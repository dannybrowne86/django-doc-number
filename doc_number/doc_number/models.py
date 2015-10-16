from django.core.urlresolvers import reverse, reverse_lazy
from django.db import models

from ata_codes.models import ATACode
from timepiece.crm.models import Business

# Create your models here.
class Document(models.Model):
    INDUSTRIES = (('A', 'Aerospace'),
                  ('C', 'Construction'),
                  ('N', 'Industrial'),
                  ('M', 'Medical'))
    DISCIPLINES = ((1, 'Solid/Surface Model'),
                   (2, 'Structural'),
                   (3, 'Mechanical'),
                   (4, 'Electrical'),
                   (5, 'Hydraulics'),
                   (6, 'Pneumatics'),
                   (7, 'Programming/Code Development'),
                   (8, 'Printed Circuit Boards'),
                   (9, 'Miscellaneous'))

    document_id = models.CharField(max_length=21)
    industry = models.CharField(max_length=1, choices=INDUSTRIES)
    business = models.ForeignKey(Business)
    ata = models.ForeignKey(ATACode)
    discipline = models.PositiveIntegerField(choices=DISCIPLINES)
    part_designator = models.PositiveIntegerField()
    serial_number = models.PositiveIntegerField()

    name = models.TextField()
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse_lazy('view_document', args=(self.pk,))

    def get_base_document_id(self):
        return '%s-%03d-%02d%02d-%d' % (self.industry, self.business.id,
                self.ata.primary_ata_code, self.ata.secondary_ata_code,
                self.discipline)

    def set_part_number(self):
        # if document_id is already set, do nothing
        if not self.document_id:
            doc_id = self.get_base_document_id()
            count = Document.objects.filter(document_id__startswith=doc_id
                ).count()
            self.part_designator = count + 1
            self.serial_number = 1
            doc_id += '-%04d-001' % (self.part_designator)
            self.document_id = doc_id
            self.save()

    def create_sub_document(self):
        print 'got to sub'
        doc_id = self.document_id[:-3]
        count = Document.objects.filter(document_id__startswith=doc_id
            ).count()
        serial_number = count + 1
        doc_id += '%03d' % (serial_number)
        doc = Document.objects.create(
            document_id=doc_id,
            industry=self.industry,
            business=self.business,
            ata=self.ata,
            discipline=self.discipline,
            part_designator=self.part_designator,
            serial_number=serial_number
        )
        return doc

    def save(self, *args, **kwargs):
        if self.id is None:
            if not self.part_designator:
                self.set_part_number()
        else:
            orig = Document.objects.get(id=self.id)
            self.document_id = orig.document_id
            self.industry = orig.industry
            self.business = orig.business
            self.ata = orig.ata
            self.part_designator = orig.part_designator
            self.serial_number = orig.serial_number
        return super(Document, self).save(*args, **kwargs)

from selectable.base import ModelLookup
from selectable.registry import registry

from .models import Document

class DocumentLookup(ModelLookup):
    model = Document
    search_fields = ('document_id__icontains', )

    def get_item_label(self, document):
        return mark_safe(u'<span class="project">%s</span>' %
                self.get_item_value(document))

    def get_item_value(self, document):
        return str(document) if document else ''

registry.register(DocumentLookup)

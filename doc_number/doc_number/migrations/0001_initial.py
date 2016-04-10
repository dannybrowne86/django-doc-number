# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ata_codes', '0001_initial'),
        ('crm', '0002_auto_20160403_1925'),
        #('crm', '0002_auto_20160409_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document_id', models.CharField(max_length=21)),
                ('industry', models.CharField(max_length=1, choices=[(b'A', b'Aerospace'), (b'C', b'Construction'), (b'N', b'Industrial'), (b'M', b'Medical')])),
                ('discipline', models.PositiveIntegerField(choices=[(1, b'Solid/Surface Model'), (2, b'Structural'), (3, b'Mechanical'), (4, b'Electrical'), (5, b'Hydraulics'), (6, b'Pneumatics'), (7, b'Programming/Code Development'), (8, b'Printed Circuit Boards'), (9, b'Miscellaneous')])),
                ('part_designator', models.PositiveIntegerField()),
                ('serial_number', models.PositiveIntegerField()),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('ata', models.ForeignKey(to='ata_codes.ATACode')),
                ('business', models.ForeignKey(to='crm.Business')),
            ],
        ),
    ]

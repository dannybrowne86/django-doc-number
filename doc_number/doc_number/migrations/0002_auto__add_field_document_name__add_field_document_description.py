# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Document.name'
        db.add_column(u'doc_number_document', 'name',
                      self.gf('django.db.models.fields.TextField')(default='Doc Name'),
                      keep_default=False)

        # Adding field 'Document.description'
        db.add_column(u'doc_number_document', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Document.name'
        db.delete_column(u'doc_number_document', 'name')

        # Deleting field 'Document.description'
        db.delete_column(u'doc_number_document', 'description')


    models = {
        u'ata_codes.atacode': {
            'Meta': {'ordering': "['primary_ata_code', 'secondary_ata_code', 'name']", 'unique_together': "(('primary_ata_code', 'secondary_ata_code'),)", 'object_name': 'ATACode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_change_date': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'primary_ata_code': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'secondary_ata_code': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'severity_factor': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'crm.business': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Business', 'db_table': "'timepiece_business'"},
            'account_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'account_owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'biz_account_holder'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'annual_revenue': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'billing_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'billing_country': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'billing_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'billing_lon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'billing_mailstop': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'billing_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'billing_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'billing_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'billing_street_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'num_of_employees': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'poc': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'business_poc_old'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'primary_contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'business_poc'", 'null': 'True', 'to': u"orm['crm.Contact']"}),
            'shipping_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'shipping_country': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'shipping_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shipping_lon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shipping_mailstop': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'shipping_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'shipping_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'shipping_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'shipping_street_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'ticker_symbol': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'crm.businessdepartment': {
            'Meta': {'object_name': 'BusinessDepartment'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bd_billing_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bd_billing_country': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'bd_billing_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bd_billing_lon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bd_billing_mailstop': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'bd_billing_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'bd_billing_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'bd_billing_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bd_shipping_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bd_shipping_country': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'bd_shipping_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bd_shipping_lon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bd_shipping_mailstop': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'bd_shipping_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'bd_shipping_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'bd_shipping_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'business': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Business']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'poc': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'business_department_poc'", 'null': 'True', 'to': u"orm['crm.Contact']"}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'crm.contact': {
            'Meta': {'ordering': "('last_name', 'first_name')", 'object_name': 'Contact'},
            'assistant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Contact']", 'null': 'True', 'blank': 'True'}),
            'assistant_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'assistant_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'assistant_phone': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'business': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Business']", 'null': 'True', 'blank': 'True'}),
            'business_department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.BusinessDepartment']", 'null': 'True', 'blank': 'True'}),
            'do_not_call': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'has_opted_out_of_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_opted_out_of_fax': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'lead_source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contact_lead_source'", 'to': u"orm['auth.User']"}),
            'mailing_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'mailing_country': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'mailing_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mailing_lon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mailing_mailstop': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'mailing_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'mailing_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'mailing_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            'office_phone': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            'other_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'other_country': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'other_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'other_lon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'other_mailstop': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'other_phone': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            'other_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'other_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'other_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'salutation': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'contact'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']", 'blank': 'True', 'unique': 'True'})
        },
        u'doc_number.document': {
            'Meta': {'object_name': 'Document'},
            'ata': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ata_codes.ATACode']"}),
            'business': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Business']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'discipline': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'document_id': ('django.db.models.fields.CharField', [], {'max_length': '21'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'part_designator': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'serial_number': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        }
    }

    complete_apps = ['doc_number']
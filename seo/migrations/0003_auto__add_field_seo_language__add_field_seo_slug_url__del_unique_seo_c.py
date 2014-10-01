# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Seo', fields ['content_type', 'object_id']
        db.delete_unique(u'seo_seo', ['content_type_id', 'object_id'])

        # Adding field 'Seo.language'
        db.add_column(u'seo_seo', 'language',
                      self.gf('django.db.models.fields.CharField')(default='fr', max_length=2),
                      keep_default=False)

        # Adding field 'Seo.slug_url'
        db.add_column(u'seo_seo', 'slug_url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'Seo', fields ['content_type', 'object_id', 'language']
        db.create_unique(u'seo_seo', ['content_type_id', 'object_id', 'language'])


    def backwards(self, orm):
        # Removing unique constraint on 'Seo', fields ['content_type', 'object_id', 'language']
        db.delete_unique(u'seo_seo', ['content_type_id', 'object_id', 'language'])

        # Deleting field 'Seo.language'
        db.delete_column(u'seo_seo', 'language')

        # Deleting field 'Seo.slug_url'
        db.delete_column(u'seo_seo', 'slug_url')

        # Adding unique constraint on 'Seo', fields ['content_type', 'object_id']
        db.create_unique(u'seo_seo', ['content_type_id', 'object_id'])


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'seo.seo': {
            'Meta': {'unique_together': "(('content_type', 'object_id', 'language'),)", 'object_name': 'Seo'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'fr'", 'max_length': '2'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'slug_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        u'seo.url': {
            'Meta': {'object_name': 'Url'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "'/'", 'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['seo']
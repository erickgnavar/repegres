# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Student.graduation_date'
        db.alter_column(u'repo_student', 'graduation_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Student.departure_date'
        db.alter_column(u'repo_student', 'departure_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Student.join_date'
        db.alter_column(u'repo_student', 'join_date', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # Changing field 'Student.graduation_date'
        db.alter_column(u'repo_student', 'graduation_date', self.gf('django.db.models.fields.DateField')(default=''))

        # Changing field 'Student.departure_date'
        db.alter_column(u'repo_student', 'departure_date', self.gf('django.db.models.fields.DateField')(default=''))

        # Changing field 'Student.join_date'
        db.alter_column(u'repo_student', 'join_date', self.gf('django.db.models.fields.DateField')(default=''))

    models = {
        'repo.language': {
            'Meta': {'object_name': 'Language'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': '2', 'max_length': '20'})
        },
        'repo.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '8'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'departure_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'graduation_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'languages': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'student_set'", 'to': "orm['repo.Language']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'repo.tmp': {
            'Meta': {'object_name': 'Tmp'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['repo.Student']", 'unique': 'True'})
        }
    }

    complete_apps = ['repo']
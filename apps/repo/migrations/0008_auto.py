# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field languages on 'Student'
        db.create_table(u'repo_student_languages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm['repo.student'], null=False)),
            ('language', models.ForeignKey(orm['repo.language'], null=False))
        ))
        db.create_unique(u'repo_student_languages', ['student_id', 'language_id'])


    def backwards(self, orm):
        # Removing M2M table for field languages on 'Student'
        db.delete_table('repo_student_languages')


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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '8'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'departure_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True'}),
            'graduation_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['repo.Language']", 'null': 'True', 'symmetrical': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
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
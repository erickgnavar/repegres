# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Language'
        db.create_table(u'repo_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=2, max_length=20)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('repo', ['Language'])

        # Adding model 'Student'
        db.create_table(u'repo_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('mobile_phone', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('join_date', self.gf('django.db.models.fields.DateField')()),
            ('departure_date', self.gf('django.db.models.fields.DateField')()),
            ('graduation_date', self.gf('django.db.models.fields.DateField')()),
            ('languages', self.gf('django.db.models.fields.related.ForeignKey')(related_name='student_set', to=orm['repo.Language'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('repo', ['Student'])


    def backwards(self, orm):
        # Deleting model 'Language'
        db.delete_table(u'repo_language')

        # Deleting model 'Student'
        db.delete_table(u'repo_student')


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
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'departure_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'graduation_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateField', [], {}),
            'languages': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'student_set'", 'to': "orm['repo.Language']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['repo']
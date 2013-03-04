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
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(related_name='language_set', to=orm['repo.Student'])),
            ('name', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('repo', ['Language'])

        # Adding model 'Student'
        db.create_table(u'repo_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=8)),
            ('first_name', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=400, null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('mobile_phone', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100, null=True)),
            ('join_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('departure_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('graduation_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('repo', ['Student'])

        # Adding model 'Tmp'
        db.create_table(u'repo_tmp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('student', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['repo.Student'], unique=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('repo', ['Tmp'])

        # Adding model 'Job'
        db.create_table(u'repo_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(related_name='job_set', to=orm['repo.Student'])),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('beginning_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('repo', ['Job'])

        # Adding model 'Certification'
        db.create_table(u'repo_certification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(related_name='certification_set', to=orm['repo.Student'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('repo', ['Certification'])


    def backwards(self, orm):
        # Deleting model 'Language'
        db.delete_table(u'repo_language')

        # Deleting model 'Student'
        db.delete_table(u'repo_student')

        # Deleting model 'Tmp'
        db.delete_table(u'repo_tmp')

        # Deleting model 'Job'
        db.delete_table(u'repo_job')

        # Deleting model 'Certification'
        db.delete_table(u'repo_certification')


    models = {
        'repo.certification': {
            'Meta': {'object_name': 'Certification'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'certification_set'", 'to': "orm['repo.Student']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'repo.job': {
            'Meta': {'object_name': 'Job'},
            'beginning_date': ('django.db.models.fields.DateField', [], {}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_set'", 'to': "orm['repo.Student']"})
        },
        'repo.language': {
            'Meta': {'object_name': 'Language'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'language_set'", 'to': "orm['repo.Student']"})
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
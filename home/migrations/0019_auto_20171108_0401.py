# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-08 04:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0039_collectionviewrestriction'),
        ('home', '0018_statsroundfifteen'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('gravitar', models.BooleanField(max_length=255, verbose_name='Use gravitar image associated with email?')),
                ('location', models.CharField(blank=True, max_length=255, verbose_name='Location (optional)')),
                ('nick', models.CharField(blank=True, max_length=255, verbose_name='Chat/Forum/IRC username (optional)')),
                ('blog', models.URLField(blank=True, verbose_name='Blog URL (not RSS URL) (optional)')),
                ('community', models.CharField(max_length=255, verbose_name='Community name')),
                ('project', models.CharField(max_length=255, verbose_name='Project description')),
                ('mentors', models.CharField(max_length=255, verbose_name='Mentor name(s)')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CohortPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('round_start', models.DateField(verbose_name='Round start date')),
                ('round_end', models.DateField(verbose_name='Round end date')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='aluminfo',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant', to='home.CohortPage'),
        ),
        migrations.AddField(
            model_name='aluminfo',
            name='picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
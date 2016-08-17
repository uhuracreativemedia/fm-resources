# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-17 16:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FileField(upload_to=b'file')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.SlugField(editable=False)),
                ('title', models.CharField(max_length=100)),
                ('menu_title', models.CharField(blank=True, max_length=100)),
                ('slug', models.SlugField(blank=True)),
                ('in_menu', models.BooleanField(db_index=True, default=True)),
                ('noindex', models.BooleanField(default=False, verbose_name=b'Do not index')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(db_index=True, default=True)),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('unpublished', models.DateTimeField(blank=True, null=True)),
                ('language', models.CharField(choices=[(b'de', b'Deutsch'), (b'en', b'English')], db_index=True, default=b'de', max_length=5)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
            ],
            options={
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resources',
            },
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ResourceCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Resource collection',
                'verbose_name_plural': 'Resource collections',
            },
        ),
        migrations.CreateModel(
            name='ResourceCollectionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort', models.PositiveSmallIntegerField()),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.ResourceCollection')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=20)),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ResourceTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Resource translation',
                'verbose_name_plural': 'Resource translations',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resources.Resource')),
                ('show_title', models.BooleanField(default=True)),
                ('meta_summary', models.TextField(blank=True)),
                ('text', models.TextField(blank=True)),
                ('template', models.CharField(blank=True, default=None, help_text='Inherit if empty', max_length=100)),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Page',
            },
            bases=('resources.resource',),
        ),
        migrations.CreateModel(
            name='Weblink',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resources.Resource')),
                ('target', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('resources.resource',),
        ),
        migrations.AddField(
            model_name='resourceproperty',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Resource'),
        ),
        migrations.AddField(
            model_name='resourcecollectionitem',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Resource'),
        ),
        migrations.AddField(
            model_name='resource',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='resource',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='resources.Resource'),
        ),
        migrations.AddField(
            model_name='resource',
            name='translation_pool',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='resources.ResourceTranslation', verbose_name='Translation pool'),
        ),
        migrations.AlterUniqueTogether(
            name='resourceproperty',
            unique_together=set([('resource', 'key')]),
        ),
        migrations.AlterUniqueTogether(
            name='resource',
            unique_together=set([('slug', 'language'), ('translation_pool', 'language')]),
        ),
    ]

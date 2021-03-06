# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 18:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteTF2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='PostAccueil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.CharField(max_length=5000)),
                ('auteur', models.CharField(max_length=50, verbose_name='publi\xe9 par')),
                ('pub_date', models.DateTimeField(verbose_name='publi\xe9 le')),
                ('edit_date', models.DateTimeField(verbose_name='modifi\xe9 le')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('content', models.TextField(max_length=10000)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteTF2.Forum')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='auteur',
        ),
        migrations.RemoveField(
            model_name='post',
            name='contenu',
        ),
        migrations.RemoveField(
            model_name='post',
            name='edit_date',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=0, max_length=10000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='siteTF2.Thread'),
            preserve_default=False,
        ),
    ]

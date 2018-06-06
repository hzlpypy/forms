# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-05 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, null=True, verbose_name='留言人')),
                ('phone', models.IntegerField(verbose_name='联系人')),
                ('content', models.TextField(verbose_name='内容')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_delete', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': '文章表',
                'verbose_name_plural': '文章表',
                'db_table': 'message',
                'ordering': ['-update_time'],
            },
        ),
    ]

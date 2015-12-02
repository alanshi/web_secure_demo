# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blog',
            },
        ),
    ]

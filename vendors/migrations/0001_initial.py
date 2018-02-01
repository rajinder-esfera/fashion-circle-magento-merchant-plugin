# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-22 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shopify', '0003_auto_20171111_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorsShopCredentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=200, null=True)),
                ('secret', models.CharField(blank=True, max_length=200, null=True)),
                ('request_token', models.CharField(blank=True, max_length=200, null=True)),
                ('request_token_secret', models.CharField(blank=True, max_length=200, null=True)),
                ('access_token', models.CharField(blank=True, max_length=200, null=True)),
                ('access_token_secret', models.CharField(blank=True, max_length=200, null=True)),
                ('platform', models.CharField(default='Shopify', max_length=100)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopify.Account')),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-06 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DnsRecord', '0006_record_resolution_line'),
    ]

    operations = [
        # migrations.AlterField(
        #     model_name='record',
        #     name='comment',
        #     field=models.CharField(blank=True, default='', help_text='备注', max_length=255, null=True, verbose_name='comment'),
        # ),
        # migrations.AlterField(
        #     model_name='record',
        #     name='expire',
        #     field=models.IntegerField(blank=True, default='', help_text='Expire time for SOA record', null=True, verbose_name='expire'),
        # ),
        # migrations.AlterField(
        #     model_name='record',
        #     name='host',
        #     field=models.CharField(blank=True, default='', help_text='Host name or IP address', max_length=255, null=True, verbose_name='host'),
        # ),
        # migrations.AlterField(
        #     model_name='record',
        #     name='minimum',
        #     field=models.IntegerField(blank=True, default='', help_text='Minimum time for SOA record(default TTL)', null=True, verbose_name='minimum'),
        # ),
        # migrations.AlterField(
        #     model_name='record',
        #     name='mx_priority',
        #     field=models.CharField(blank=True, default='', help_text='MX Priority', max_length=255, null=True, verbose_name='mx_priority'),
        # ),
        # migrations.AlterField(
        #     model_name='record',
        #     name='primary_ns',
        #     field=models.CharField(blank=True, default='', help_text='Primary name server for SOA record', max_length=255, null=True, verbose_name='primary_ns'),
        # ),
        # migrations.AlterField(
        #     model_name='record',
        #     name='refresh',
        #     field=models.IntegerField(blank=True, default='', help_text='Refresh time for SOA record', null=True, verbose_name='refresh'),
        # ),
        # migrations.AlterField(
        #     model_name='record',
        #     name='resp_person',
        #     field=models.CharField(blank=True, default='', help_text='Responsible person mail for SOA record', max_length=255, null=True, verbose_name='resp_person'),
        # ),
        # migrations.AlterField(
        #     model_name='record',
        #     name='retry',
        #     field=models.IntegerField(blank=True, default='', help_text='Retry time for SOA record', null=True, verbose_name='retry'),
        # ),
        # migrations.AlterField(
        #     model_name='record',
        #     name='serial',
        #     field=models.BigIntegerField(blank=True, default='', help_text='serial # for SOA record', null=True, verbose_name='serial'),
        # ),
        # migrations.AlterField(
        #     model_name='record',
        #     name='ttl',
        #     field=models.IntegerField(blank=True, default='', help_text='Time to live', null=True, verbose_name='ttl'),
        # ),
        # migrations.AlterField(
        #     model_name='record',
        #     name='type',
        #     field=models.CharField(blank=True, choices=[('A', 'A'), ('CNAME', 'CNAME'), ('MX', 'MX'), ('TXT', 'TXT'), ('NS', 'NS'), ('AAAA', 'AAAA'), ('SRV', 'SRV'), ('PTR', 'PTR'), ('SOA', 'SOA')], default='', help_text='DNS data type', max_length=64, null=True, verbose_name='type'),
        # ),
    ]

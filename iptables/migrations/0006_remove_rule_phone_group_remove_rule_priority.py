# Generated by Django 4.1.6 on 2023-02-21 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iptables', '0005_alter_iptable_ip_address_alter_rule_phone_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rule',
            name='phone_group',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='priority',
        ),
    ]

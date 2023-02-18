# Generated by Django 4.1.6 on 2023-02-16 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_blackphone_created_at_whitephone_created_at'),
        ('iptables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='规则名称')),
                ('priority', models.IntegerField(verbose_name='优先级')),
                ('callee_prefix', models.CharField(max_length=10, verbose_name='被叫前缀')),
                ('ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iptables.iptable', verbose_name='IP地址')),
                ('phone_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.blackphone', verbose_name='黑名单组')),
            ],
            options={
                'verbose_name_plural': '规则设置',
            },
        ),
    ]

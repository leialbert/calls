# Generated by Django 4.1.6 on 2023-02-18 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_alter_level_options_level_group_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='group_type',
            field=models.CharField(choices=[('black', '黑名单'), ('white', '白名单')], max_length=8, verbose_name='群组类型'),
        ),
    ]

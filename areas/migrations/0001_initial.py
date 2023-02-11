# Generated by Django 4.1.6 on 2023-02-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(max_length=7, verbose_name='手机前缀')),
                ('area_code', models.CharField(max_length=4, verbose_name='地区区号')),
                ('area_name', models.CharField(max_length=10, verbose_name='地区名称')),
                ('mobile_carrier', models.CharField(max_length=8, verbose_name='运营商')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
            },
        ),
    ]

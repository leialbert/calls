# Generated by Django 4.1.6 on 2023-02-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_blackphone_created_at_whitephone_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=12, verbose_name='自定义组')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
    ]

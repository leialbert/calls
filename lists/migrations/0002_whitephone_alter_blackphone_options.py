# Generated by Django 4.1.6 on 2023-02-15 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhitePhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(choices=[(0, '自定义组1'), (1, '自定义组2'), (2, '自定义组3')], verbose_name='级别')),
                ('phone', models.CharField(max_length=11, verbose_name='号码')),
            ],
            options={
                'verbose_name': '白名单号码',
                'verbose_name_plural': '白名单号码',
            },
        ),
        migrations.AlterModelOptions(
            name='blackphone',
            options={'verbose_name': '黑名单号码', 'verbose_name_plural': '黑名单号码'},
        ),
    ]

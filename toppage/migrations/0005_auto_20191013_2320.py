# Generated by Django 2.1 on 2019-10-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toppage', '0004_auto_20191013_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='address2',
            field=models.CharField(blank=True, max_length=100, verbose_name='所在地名2'),
        ),
    ]

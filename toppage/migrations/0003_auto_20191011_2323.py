# Generated by Django 2.1 on 2019-10-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toppage', '0002_article_pictureflag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pictureFlag',
            field=models.CharField(blank=True, max_length=10, verbose_name='写真有無'),
        ),
    ]

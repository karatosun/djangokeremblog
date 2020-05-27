# Generated by Django 3.0.6 on 2020-05-22 08:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Makaleye Fotoğraf Ekleyin'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Güncellenme Tarihi'),
        ),
    ]
# Generated by Django 3.0.6 on 2020-05-27 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20200527_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Onay'),
        ),
    ]
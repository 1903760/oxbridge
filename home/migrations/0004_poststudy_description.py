# Generated by Django 2.0.5 on 2018-05-29 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_poststudy'),
    ]

    operations = [
        migrations.AddField(
            model_name='poststudy',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='описание'),
        ),
    ]

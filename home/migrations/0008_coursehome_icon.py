# Generated by Django 2.0.5 on 2018-05-31 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_coursehome_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursehome',
            name='icon',
            field=models.CharField(blank=True, default=None, max_length=20, verbose_name='иконка'),
        ),
    ]

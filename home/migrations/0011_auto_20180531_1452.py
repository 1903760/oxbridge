# Generated by Django 2.0.5 on 2018-05-31 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20180531_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursehome',
            old_name='descriptions',
            new_name='description',
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-29 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_auto_20180529_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('phone', models.CharField(max_length=50, verbose_name='телефон')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
                ('house', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.Test', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки с тестом',
                'ordering': ['date'],
            },
        ),
    ]

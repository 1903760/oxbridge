# Generated by Django 2.0.5 on 2018-05-28 06:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, verbose_name='ответ')),
                ('rights', models.SmallIntegerField(blank=True, db_index=True, default=None, verbose_name='бал')),
            ],
            options={
                'verbose_name': 'ответ',
                'verbose_name_plural': 'ответы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, verbose_name='Вопрос')),
                ('rights', models.SmallIntegerField(blank=True, db_index=True, default=None, verbose_name='порядок')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['rights'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=50, verbose_name='ФИО')),
                ('text', models.TextField(blank=True, default=None, verbose_name='Отзыв')),
                ('date_review', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='дата отзыва')),
                ('fs', models.CharField(blank=True, max_length=130, verbose_name='фейсбук')),
                ('inst', models.CharField(blank=True, max_length=130, verbose_name='инстаграмм')),
                ('vk', models.CharField(blank=True, max_length=130, verbose_name='вк')),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'отзывы',
                'ordering': ['date_review'],
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, verbose_name='название теста')),
                ('slug', models.SlugField(blank=True, verbose_name='название для ссылки')),
            ],
            options={
                'verbose_name': 'тест',
                'verbose_name_plural': 'тесты',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.Test', verbose_name='тест'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.Question', verbose_name='вопрос'),
        ),
    ]

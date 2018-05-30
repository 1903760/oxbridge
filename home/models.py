from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from easy_thumbnails.fields import ThumbnailerImageField


class Review(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=50, default=None, blank=True)
    text = models.TextField(verbose_name='Отзыв', default=None, blank=True)
    img = ThumbnailerImageField(verbose_name='автар', upload_to='review/', blank=True)
    date_review = models.DateField(verbose_name='дата отзыва', default=timezone.now, blank=True)
    fs = models.CharField(verbose_name='фейсбук', max_length=130, blank=True)
    inst = models.CharField(verbose_name='инстаграмм', max_length=130, blank=True)
    vk = models.CharField(verbose_name='вк', max_length=130, blank=True)

    class Meta:
        verbose_name_plural = 'отзывы'
        verbose_name = 'отзыв'
        ordering = ['date_review']

    def __str__(self):
        return '{}'.format(self.name)


class Test(models.Model):
    name = models.CharField(verbose_name='название теста', max_length=60, blank=True)
    slug = models.SlugField(verbose_name='название для ссылки', blank=True)
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name_plural = 'тесты'
        verbose_name = 'тест'
        ordering = ['name']

    def __str__(self):
        return '{}'.format(self.name)

    @cached_property
    def questions(self):
        return self.question_set.all()


class Question(models.Model):
    name = models.CharField(verbose_name='Вопрос', max_length=300, blank=True)
    test = models.ForeignKey(Test, verbose_name='тест', on_delete=models.CASCADE, blank=True)
    rights = models.SmallIntegerField(verbose_name='порядок', default=None, blank=True, db_index=True)

    class Meta:
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'
        ordering = ['rights']

    def __str__(self):
        return '{}'.format(self.name)

    @cached_property
    def answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    name = models.CharField(verbose_name='ответ', max_length=300, blank=True)
    question = models.ForeignKey(Question, verbose_name='вопрос', on_delete=models.CASCADE, blank=True)
    rights = models.SmallIntegerField(verbose_name='балы', default=None, blank=True, db_index=True)

    class Meta:
        verbose_name_plural = 'ответы'
        verbose_name = 'ответ'
        ordering = ['name']

    def __str__(self):
        return '{}'.format(self.name)


class PostStudy(models.Model):
    name = models.CharField(verbose_name='название', max_length=300, blank=True)
    img = ThumbnailerImageField(verbose_name='картинка', upload_to='study/', blank=True)
    description = models.TextField(verbose_name='описание', default='', blank=True)

    class Meta:
        verbose_name_plural = 'Преимущества обучения'
        verbose_name = 'Преимущества обучения'
        ordering = ['name']

    def __str__(self):
        return '{}'.format(self.name)


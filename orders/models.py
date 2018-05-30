from django.db import models
from home.models import Test
# Create your models here.


class ScoringScale(models.Model):
    name = models.CharField(verbose_name='название уровня', max_length=50, blank=True)
    balls = models.SmallIntegerField(verbose_name='количество баллов', default=None, blank=True)

    class Meta:
        verbose_name = 'Уровень английского'
        verbose_name_plural = 'Уровни английского'
        ordering = ['name']

    def __str__(self):
        return self.name


class Order(models.Model):
    # test = models.ForeignKey(Test, verbose_name="Тест", on_delete=models.CASCADE, blank=True)
    name = models.CharField("имя", max_length=50)
    phone = models.CharField("телефон", max_length=50)
    level = models.ForeignKey(ScoringScale, verbose_name='уровень', on_delete=models.CASCADE)
    date = models.DateTimeField("дата", auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки с тестом'
        ordering = ['date']

    def __str__(self):
        return self.name

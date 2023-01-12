from django.db import models

from .utils import from_cyrillic_to_eng


class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Название населенного пункта',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)
    
    
    class Meta:
        verbose_name = 'Название населенного пункта'
        verbose_name_plural = 'Название населенных пунктов'


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Вид работы',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Вид работы'

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)

class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Загаловок вакансии')
    company = models.CharField(max_length=250, verbose_name='Работодатель')
    description = models.TextField(verbose_name='Описание вакансии')
    tel = models.CharField(max_length=20, verbose_name='Телефон')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='Сфера деятельности')
    timestamp = models.DateField(auto_now_add=True,)


    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title





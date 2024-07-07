from django.db import models


class Post(models.Model):
    title = models.CharField('Название', max_length=64)
    content = models.TextField('Контент')
    created_at = models.DateTimeField('Дата и время создания',
                                      auto_now_add=True)
    updated_at = models.DateTimeField('Дата и время обновления',
                                      auto_now=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.title} ({self.pk})'

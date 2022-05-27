from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Topic(models.Model):
    name = models.CharField(max_length=50, verbose_name='Раздел',)
    topiks = models.ManyToManyField(Article, through ='Scope', related_name='topics',)

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Topic, on_delete=models.CASCADE)
    topic = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return '{0}_{1}'.format(self.article, self.topic)
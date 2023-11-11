from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Описание')
    email = models.EmailField('email')
    VALUECATEGORY = [('3D','3D-Дизайн'),('2D','2D-Дизайн'),('sketch','Эскиз'),('Other','Прочее')]
    category = models.CharField('Категория', max_length=50, choices=VALUECATEGORY)
    name = models.CharField('Имя', max_length=1478)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "заявка"
        verbose_name_plural = "Заявки"
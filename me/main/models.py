from email.policy import default
from django.db import models

class Facts(models.Model):
    title = models.CharField('Название факта', max_length=50)
    fact = models.TextField('Описание', blank=True)
    published = models.DateField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Факт"
        verbose_name_plural = "Факты"
        ordering = ['published']
        
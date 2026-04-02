from django.db import models


class Task(models.Model):
    '''Модель вопроса игры'''
    text = models.CharField("Вопрос", max_length=255)
    option1 = models.CharField("Вариант 1", max_length=100)
    option2 = models.CharField("Вариант 2", max_length=100)
    correct = models.CharField("Правильный ответ", max_length=100)

    def __str__(self):
        return str(self.text)
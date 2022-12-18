from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField('Название продукта', max_length=50)
    carbs = models.FloatField('углеводы')
    protein = models.FloatField('белки')
    fats = models.FloatField('жиры')
    calories = models.IntegerField('Количество калорий')

class Consume(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)


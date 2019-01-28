from django.db import models
import datetime


class Lunch(models.Model):
    nickname = models.CharField(max_length=100, default='')
    user = models.CharField(max_length=100, default='')
    date = models.DateField(max_length=100, default=datetime.date.today)

    def __str__(self):
        return self.nickname


class Location(models.Model):
    lunch = models.ForeignKey('tavern.Lunch', on_delete=models.CASCADE, null=True)
    restaurant_suggestions = models.CharField(max_length=100, null=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.restaurant_suggestions

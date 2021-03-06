# Generated by Django 2.1.5 on 2019-01-28 01:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tavern', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='lunch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tavern.Lunch'),
        ),
        migrations.AddField(
            model_name='location',
            name='restaurant_suggestions',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lunch',
            name='date',
            field=models.DateField(default=datetime.date.today, max_length=100),
        ),
        migrations.AddField(
            model_name='lunch',
            name='nickname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='lunch',
            name='user',
            field=models.CharField(default='', max_length=100),
        ),
    ]

# Generated by Django 2.1.5 on 2019-01-28 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tavern', '0003_auto_20190128_0256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='title',
            new_name='restaurant_suggestions',
        ),
    ]
# Generated by Django 3.1.1 on 2020-09-17 17:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeQuiz', '0006_auto_20200918_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeequiz',
            name='time_answered',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 17, 17, 51, 53, 39132, tzinfo=utc)),
        ),
    ]

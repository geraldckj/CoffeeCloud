# Generated by Django 3.1.1 on 2020-09-18 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeCloud', '0014_dailylog_datelogged'),
    ]

    operations = [
        migrations.AddField(
            model_name='beans',
            name='intendedBrewMethod',
            field=models.CharField(default='Filter', max_length=100),
        ),
    ]

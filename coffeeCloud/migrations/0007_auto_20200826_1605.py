# Generated by Django 3.1 on 2020-08-26 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coffeeCloud', '0006_auto_20200825_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailylog',
            name='bean',
        ),
        migrations.AddField(
            model_name='beans',
            name='notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='beans',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailylog',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='coffeeCloud.beans'),
            preserve_default=False,
        ),
    ]
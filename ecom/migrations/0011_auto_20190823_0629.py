# Generated by Django 2.1.7 on 2019-08-23 06:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0010_history_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
# Generated by Django 3.2 on 2023-04-14 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20230413_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytododone',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

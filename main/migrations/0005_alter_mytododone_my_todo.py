# Generated by Django 3.2 on 2023-04-14 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_mytododone_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytododone',
            name='my_todo',
            field=models.ManyToManyField(to='main.ToDo'),
        ),
    ]
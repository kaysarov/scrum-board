# Generated by Django 2.1.2 on 2018-10-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.DateField(blank=True, verbose_name='Выполнено'),
        ),
    ]

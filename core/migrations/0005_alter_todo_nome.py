# Generated by Django 4.1 on 2022-09-18 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_todo_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='nome',
            field=models.CharField(max_length=36),
        ),
    ]

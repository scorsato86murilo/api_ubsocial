# Generated by Django 5.1.7 on 2025-03-16 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='curso',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-15 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppQuiz', '0004_alter_result_options_remove_result_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='score',
            field=models.IntegerField(),
        ),
    ]

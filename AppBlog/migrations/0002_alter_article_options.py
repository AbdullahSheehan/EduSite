# Generated by Django 4.2.6 on 2023-10-14 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publish']},
        ),
    ]
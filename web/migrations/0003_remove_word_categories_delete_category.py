# Generated by Django 4.2.7 on 2023-11-06 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_category_word_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-06 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_word_categories_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='synonymns',
            field=models.CharField(default='hi', max_length=255),
            preserve_default=False,
        ),
    ]
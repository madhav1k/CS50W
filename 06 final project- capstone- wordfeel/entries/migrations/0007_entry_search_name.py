# Generated by Django 5.0.2 on 2024-04-19 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0006_rename_specialized_name_entry_wiktionary_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='search_name',
            field=models.CharField(default=models.CharField(max_length=200), max_length=200),
        ),
    ]

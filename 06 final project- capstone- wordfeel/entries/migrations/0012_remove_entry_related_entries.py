# Generated by Django 5.0.2 on 2024-04-20 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0011_remove_entry_meaning'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='related_entries',
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-13 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_event_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='start_date',
        ),
    ]

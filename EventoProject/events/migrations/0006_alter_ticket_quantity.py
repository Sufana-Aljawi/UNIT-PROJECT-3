# Generated by Django 4.2.7 on 2023-12-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_ticket_delete_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]

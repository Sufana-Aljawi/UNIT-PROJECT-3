# Generated by Django 4.2.7 on 2023-12-09 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Art', 'Art'), ('Technology', 'Technology'), ('Entertainment', 'Entertainment'), ('Exclusive', 'Exclusive')], max_length=100),
        ),
    ]

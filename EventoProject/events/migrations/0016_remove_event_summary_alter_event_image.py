# Generated by Django 4.2.7 on 2023-12-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_alter_event_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='summary',
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='images/defult.jpg', upload_to='images/'),
        ),
    ]

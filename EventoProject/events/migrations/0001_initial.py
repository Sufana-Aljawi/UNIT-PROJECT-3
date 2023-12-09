# Generated by Django 4.2.7 on 2023-12-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2010)),
                ('content', models.TextField()),
                ('posting_date', models.DateField()),
                ('category', models.CharField(choices=[('Art', 'Art'), ('Healthcare', 'Healthcare'), ('Technology', 'Technology'), ('Entertainment', 'Entertainment')], max_length=80)),
                ('image', models.ImageField(default='images/default.jpg', upload_to='images/')),
            ],
        ),
    ]

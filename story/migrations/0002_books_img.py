# Generated by Django 3.2.7 on 2021-10-05 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='img',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]

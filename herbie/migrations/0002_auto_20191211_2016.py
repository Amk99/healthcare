# Generated by Django 2.2.5 on 2019-12-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonies',
            name='img',
            field=models.ImageField(upload_to='media'),
        ),
    ]

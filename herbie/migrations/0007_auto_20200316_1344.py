# Generated by Django 2.2.5 on 2020-03-16 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbie', '0006_auto_20200316_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_blog',
            name='image_three',
        ),
        migrations.AlterField(
            model_name='my_blog',
            name='intro',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='my_blog',
            name='quote',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]

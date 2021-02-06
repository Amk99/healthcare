# Generated by Django 2.2.5 on 2020-03-16 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbie', '0005_my_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_blog',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='my_blog',
            name='image_three',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='my_blog',
            name='image_two',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='my_blog',
            name='intro',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='my_blog',
            name='quote',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
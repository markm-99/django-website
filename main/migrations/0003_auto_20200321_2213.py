# Generated by Django 2.0 on 2020-03-22 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='averageRating',
            field=models.FloatField(default=0),
        ),
    ]

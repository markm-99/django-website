# Generated by Django 2.1.5 on 2020-11-28 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20201128_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.URLField(default=None, null=True),
        ),
    ]

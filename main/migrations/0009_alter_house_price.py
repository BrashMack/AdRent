# Generated by Django 5.0 on 2023-12-14 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_house_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.FloatField(verbose_name='цена'),
        ),
    ]

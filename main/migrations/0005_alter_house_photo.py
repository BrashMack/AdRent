# Generated by Django 5.0 on 2023-12-14 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_house_id_arend_remove_house_timees_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='photo',
            field=models.ImageField(max_length=15, upload_to='', verbose_name='фото'),
        ),
    ]

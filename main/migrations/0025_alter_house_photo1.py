# Generated by Django 4.1.7 on 2023-12-16 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_house_photo1_alter_house_photo2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='photo1',
            field=models.ImageField(default='Нет фото', upload_to='static/images', verbose_name='фото'),
        ),
    ]

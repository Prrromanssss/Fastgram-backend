# Generated by Django 3.2.16 on 2022-12-19 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0004_alter_mainimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainimage',
            name='image',
            field=models.ImageField(default='./static_dev/img/blank_avatar.jpeg', upload_to='previews/%Y/%m/%d', verbose_name='изображение'),
        ),
    ]

# Generated by Django 3.2.16 on 2022-12-19 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='previews/blank_avatar.jpeg', upload_to='previews/%Y/%m/%d', verbose_name='изображение'),
        ),
    ]
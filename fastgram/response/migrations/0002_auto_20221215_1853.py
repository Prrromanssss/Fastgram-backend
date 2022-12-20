# Generated by Django 3.2.16 on 2022-12-15 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='опубликовано'),
        ),
        migrations.AlterField(
            model_name='mainimage',
            name='image',
            field=models.ImageField(upload_to='previews/%Y/%m/%d', verbose_name='изображение к отзыву'),
        ),
    ]
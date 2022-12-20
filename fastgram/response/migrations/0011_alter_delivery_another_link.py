# Generated by Django 3.2.16 on 2022-12-19 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0010_delivery_another_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='another_link',
            field=models.URLField(blank=True, help_text='Добавьте ссылку на сайт с отзывами об этой службе', null=True, verbose_name='другие отзывы'),
        ),
    ]

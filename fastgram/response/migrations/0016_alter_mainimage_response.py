# Generated by Django 3.2.16 on 2022-12-20 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0015_auto_20221219_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainimage',
            name='response',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='response.response', verbose_name='отзыв'),
        ),
    ]
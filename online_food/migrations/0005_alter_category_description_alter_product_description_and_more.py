# Generated by Django 4.1.5 on 2023-01-23 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_food', '0004_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
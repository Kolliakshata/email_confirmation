# Generated by Django 4.2 on 2023-04-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_ingredient_remove_menu_ingredients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='calories_per_serving',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='serving_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

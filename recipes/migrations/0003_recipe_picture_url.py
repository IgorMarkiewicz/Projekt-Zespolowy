# Generated by Django 5.0.3 on 2024-04-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_rating_user_alter_recipe_user_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='picture_url',
            field=models.URLField(default='https://cdn.georgeinstitute.org/sites/default/files/styles/width1920_fallback/public/2020-10/world-food-day-2020.png'),
        ),
    ]

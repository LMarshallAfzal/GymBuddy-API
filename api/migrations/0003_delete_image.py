# Generated by Django 5.0 on 2023-12-26 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_exercise_image1_exercise_image2_exercise_image3_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
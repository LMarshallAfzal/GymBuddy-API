# Generated by Django 5.0 on 2023-12-30 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='image1',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='image2',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='image3',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='image4',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]

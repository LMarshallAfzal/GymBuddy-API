# Generated by Django 5.0 on 2023-12-26 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=25, null=True)),
                ('muscle_group', models.CharField(blank=True, max_length=30, null=True)),
                ('equipment', models.CharField(blank=True, max_length=15, null=True)),
                ('level', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'ordering': ['muscle_group'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['url'],
            },
        ),
    ]

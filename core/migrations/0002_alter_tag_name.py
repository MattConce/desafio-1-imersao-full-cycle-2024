# Generated by Django 5.1.2 on 2024-10-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nome'),
        ),
    ]
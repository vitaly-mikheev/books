# Generated by Django 3.2.8 on 2021-10-28 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='release_date',
            field=models.DateField(),
        ),
    ]
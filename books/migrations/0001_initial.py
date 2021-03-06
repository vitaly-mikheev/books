# Generated by Django 3.2.8 on 2021-10-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('synopsis', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('release_date', models.DateField(auto_now_add=True)),
                ('price_in_cents', models.IntegerField()),
            ],
        ),
    ]

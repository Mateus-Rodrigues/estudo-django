# Generated by Django 5.2.3 on 2025-06-18 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('factory_year', models.IntegerField()),
                ('model_year', models.IntegerField(blank=True, null=True)),
                ('values', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]

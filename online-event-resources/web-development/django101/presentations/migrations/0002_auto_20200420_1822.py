# Generated by Django 3.0.5 on 2020-04-20 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

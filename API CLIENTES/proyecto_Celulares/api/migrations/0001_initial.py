# Generated by Django 3.2.4 on 2022-04-21 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celulares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificación', models.PositiveIntegerField()),
                ('númeroDeProductosVendidos', models.PositiveIntegerField()),
            ],
        ),
    ]

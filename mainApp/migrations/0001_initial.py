# Generated by Django 4.1.2 on 2022-11-28 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]

# Generated by Django 2.0.4 on 2018-05-02 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20180423_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserScore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('levelId', models.IntegerField()),
                ('moves', models.IntegerField()),
                ('time', models.TextField()),
            ],
        ),
    ]

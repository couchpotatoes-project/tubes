# Generated by Django 2.0.4 on 2018-04-24 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20180423_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

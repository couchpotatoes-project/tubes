# Generated by Django 2.0.4 on 2018-04-24 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='level',
            name='levelId',
            field=models.IntegerField(),
        ),
    ]

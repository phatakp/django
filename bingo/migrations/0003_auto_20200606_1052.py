# Generated by Django 3.0.6 on 2020-06-06 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bingo', '0002_auto_20200606_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
# Generated by Django 2.2.3 on 2019-12-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20191227_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default='2019-12-31'),
        ),
    ]

# Generated by Django 2.2.3 on 2019-12-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20191227_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.TextField(default=''),
        ),
    ]

# Generated by Django 3.1.7 on 2021-05-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20210518_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_boy',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0006_auto_20200410_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]

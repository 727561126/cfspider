# Generated by Django 2.2.1 on 2019-05-29 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfmodel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fhmodel',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
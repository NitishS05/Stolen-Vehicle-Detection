# Generated by Django 4.1.3 on 2023-01-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='mobile',
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]
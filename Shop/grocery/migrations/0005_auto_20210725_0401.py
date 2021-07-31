# Generated by Django 3.1 on 2021-07-25 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0004_auto_20210724_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='date',
        ),
        migrations.AddField(
            model_name='items',
            name='ordered_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='items',
            name='timestamp',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
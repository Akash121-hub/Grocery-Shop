# Generated by Django 3.1 on 2021-07-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0003_auto_20210724_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

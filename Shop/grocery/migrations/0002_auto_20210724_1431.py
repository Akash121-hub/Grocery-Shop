# Generated by Django 3.1 on 2021-07-24 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='items',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='grocery.customer'),
            preserve_default=False,
        ),
    ]

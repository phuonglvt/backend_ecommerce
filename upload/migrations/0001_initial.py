# Generated by Django 4.2.11 on 2024-04-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=255)),
                ('filename', models.CharField(max_length=255)),
                ('format', models.CharField(default='png', max_length=16)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

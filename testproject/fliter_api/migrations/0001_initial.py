# Generated by Django 3.2.6 on 2021-08-26 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filter_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(blank=True, max_length=266, null=True)),
                ('timestamp_at', models.DateTimeField(blank=True, max_length=266, null=True)),
                ('publisher_id', models.CharField(blank=True, max_length=266, null=True)),
                ('shopper_id', models.CharField(blank=True, max_length=266, null=True)),
            ],
        ),
    ]

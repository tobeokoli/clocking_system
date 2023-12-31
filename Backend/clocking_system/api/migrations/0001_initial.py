# Generated by Django 4.2.4 on 2023-08-20 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clock_in_time', models.DateTimeField(auto_now_add=True)),
                ('clock_out_time', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('has_clocked_out', models.BooleanField(default=False)),
            ],
        ),
    ]

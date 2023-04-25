# Generated by Django 4.2 on 2023-04-18 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=10)),
                ('state', models.CharField(choices=[('Iran, IR', 'Iran'), ('Texas, TX', 'Texas'), ('Alabama, AL', 'Alabama')], default='Alabama, AL', max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('other', models.CharField(max_length=50)),
                ('start_date', models.CharField(max_length=25)),
                ('end_date', models.CharField(max_length=25)),
                ('category', models.CharField(max_length=25)),
                ('list_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
    ]
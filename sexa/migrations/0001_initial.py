# Generated by Django 3.1.4 on 2020-12-26 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('review', models.TextField()),
                ('review2', models.TextField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]

# Generated by Django 3.2.3 on 2021-07-06 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_url', models.CharField(max_length=1000)),
                ('new_url', models.CharField(max_length=10)),
                ('time_created', models.DateTimeField()),
            ],
        ),
    ]

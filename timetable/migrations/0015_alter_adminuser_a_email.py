# Generated by Django 3.2.19 on 2023-06-30 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0014_alter_adminuser_a_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='a_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]

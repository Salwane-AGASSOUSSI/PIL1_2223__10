# Generated by Django 3.2.19 on 2023-06-29 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_rename_emploi_emploidutemps_emploi_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='emploidutemps',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-06 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workevidence', '0002_alter_workevidence_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workevidence',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-06 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workevidence', '0003_alter_workevidence_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workevidence',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

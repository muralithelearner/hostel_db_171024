# Generated by Django 5.0.8 on 2024-08-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp20', '0005_remove_addproperty_free_rooms_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproperty',
            name='free_beds',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='addproperty',
            name='occupied_beds',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='addproperty',
            name='total_rooms',
            field=models.IntegerField(default=0),
        ),
    ]
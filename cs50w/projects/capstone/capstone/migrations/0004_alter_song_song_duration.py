# Generated by Django 4.1.3 on 2022-12-27 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0003_alter_category_id_alter_song_id_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_duration',
            field=models.TimeField(max_length=1000),
        ),
    ]

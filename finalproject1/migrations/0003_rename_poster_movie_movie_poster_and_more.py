# Generated by Django 4.0.6 on 2022-07-20 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalproject1', '0002_movie_main_actors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='poster',
            new_name='Movie_poster',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='trailer_field',
            new_name='Movie_trailer',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='release_date',
            new_name='released_date',
        ),
    ]

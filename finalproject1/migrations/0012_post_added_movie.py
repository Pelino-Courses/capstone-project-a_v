# Generated by Django 4.0.6 on 2022-08-05 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalproject1', '0011_alter_contact_email_favorite_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_added',
            name='movie',
            field=models.FileField(blank=True, null=True, upload_to='movies'),
        ),
    ]

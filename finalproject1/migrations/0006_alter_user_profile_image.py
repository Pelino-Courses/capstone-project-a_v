# Generated by Django 4.0.6 on 2022-07-26 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalproject1', '0005_alter_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

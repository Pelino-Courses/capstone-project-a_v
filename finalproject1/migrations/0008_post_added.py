# Generated by Django 4.0.6 on 2022-08-03 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalproject1', '0007_signin_remove_movie_uploaded_by_remove_user_groups_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='post_added',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_title', models.CharField(max_length=250)),
                ('m_description', models.TextField()),
                ('realese_date', models.DateField()),
                ('m_flyer', models.ImageField(default='mdefault.jpg', upload_to='movies')),
                ('m_actors', models.CharField(max_length=255)),
                ('m_trailer', models.CharField(max_length=250)),
                ('m_genre', models.CharField(max_length=256)),
                ('posted_date', models.DateTimeField()),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finalproject1.signin')),
            ],
        ),
    ]

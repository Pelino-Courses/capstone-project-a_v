# Generated by Django 4.0.6 on 2022-08-04 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalproject1', '0010_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.CreateModel(
            name='favorite_movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finalproject1.post_added')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finalproject1.signin')),
            ],
        ),
    ]

from distutils.command.upload import upload
from tkinter import CASCADE
from turtle import width
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class signin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    gender=(
        ("Female",'F'),
        ("Male",'M'),
        ("Others",'O')
    )
    gender=models.CharField(max_length=10, choices=gender)
    Avatar=models.ImageField(default='default.png', upload_to='profile_images')

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"

    def save(self,*args,**kwargs):
        super(signin,self).save(*args,**kwargs)

        img=Image.open(self.Avatar.path)

        if img.height>500 or img.width>500:
            size_img=(500,500)
            img.thumbnail(size_img)
            img.save(self.Avatar.path)
class post_added(models.Model):
    posted_by=models.ForeignKey(signin,  on_delete=models.CASCADE)
    m_title=models.CharField(max_length=250)
    m_description=models.TextField()
    realese_date=models.DateField()
    m_flyer=models.ImageField(default='mdefault.jpg', upload_to='movies')
    m_actors=models.CharField(max_length=255)
    m_trailer=models.CharField(max_length=250)
    movie=models.FileField(upload_to='movies', blank=True,null=True)
    m_genre=models.CharField(max_length=256)
    posted_date=models.DateTimeField()

    def __str__(self):
        return self.m_title
    
    def save(self, *args, **kwargs):
        super(post_added,self).save(*args,**kwargs)

        img=Image.open(self.m_flyer.path)

        if img.height>400 and img.width>400:
            img_size=(400,400)
            img.thumbnail(img_size)
            img.save(self.m_flyer.path)

class favorite_movie(models.Model):
    movie_title=models.ForeignKey(post_added, on_delete=models.CASCADE)
    uploader=models.ForeignKey(signin, on_delete=models.CASCADE)
    
    

class contact(models.Model):
    names=models.CharField(max_length=255)
    email=models.EmailField()
    m_message=models.TextField()

    def __str__(self):
        return self.names




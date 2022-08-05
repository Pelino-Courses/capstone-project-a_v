from unicodedata import name
from django.urls import path
from .views import User_registration,favorite,callsearch,callplay, callabout,dashboard,callprofile,login_user,ad_contact,callindex,callpost,user_logout,ad_post
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('signin/',User_registration, name="signin"),
    path('dashboard/',dashboard, name="dashboard"),
    path('login/',login_user, name="login"),
    path('',callindex, name='index'),
    path('post/',callpost, name='post1'),
    path('about/',callabout, name='about'),
    path('contact/',ad_contact, name='contact_us'),
    path('logout/' ,user_logout, name="logout"),
    path('ad_post/',ad_post,name="post"),
    path('profile/',callprofile,name="profile1"),
    path('fav/<str:movie_id>&<str:user_id>',favorite,name="fav"),
    path('search', callsearch, name="search"),
    path('play/<str:movie_id>', callplay, name="play_movie")





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
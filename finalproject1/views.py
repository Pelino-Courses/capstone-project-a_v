from cgitb import text
import email
from hashlib import new
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import signin,post_added,contact,favorite_movie
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import user_logged_out
from django.views.decorators.cache import cache_control




# Create your views here.

def User_registration(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        if request.method=="POST" and request.FILES:
            first_name=request.POST['fname']
            last_name=request.POST['lname']
            email=request.POST['email']
            age=request.POST['age']
            gender=request.POST['gender']
            password=request.POST['psw']
            Profile_img=request.FILES.get('profile')

            create_user=User(
                username=email,
                first_name=first_name,
                last_name=last_name,
                email=email,
                date_joined=datetime.datetime.now()  )
            
            create_user.set_password(password)
            create_user.save()

            signin.objects.create(
                user=create_user,
                age=age,
                gender=gender,
                Avatar=Profile_img
            )
            messages.success(request,"Thank you for creating Account!!!!!!")
            return redirect("login")
        elif request.method=="POST":
            first_name=request.POST['fname']
            last_name=request.POST['lname']
            email=request.POST['email']
            age=request.POST['age']
            gender=request.POST['gender']
            password=request.POST['psw']

            create_user=User(
                username=email,
                first_name=first_name,
                last_name=last_name,
                email=email,
                date_joined=datetime.datetime.now()  )
            
            create_user.set_password(password)
            create_user.save()

            signin.objects.create(
                user=create_user,
                age=age,
                gender=gender
            )
            messages.success(request,"Thank you for creating Account!!!!!!")
            return redirect("login")
        return render (request, "signin.html",{})



@cache_control(no_cache=True, must_revalidate=True, no_strore=True)
@login_required(login_url="login")
def dashboard(request):
    mov=post_added.objects.all()
    context={'mov':mov}
    return render(request,"dashboard.html",context)

def login_user(request):

        if request.method=="POST":
            username=request.POST['user_name']
            password=request.POST['psw']

            log_user=authenticate(request,username=username,password=password)
            if log_user is not None:
                login(request,log_user)
                return redirect("dashboard")
            else:
                messages.info(request,"Username or Password is Wrong")
        return render(request,"login.html",{})

def user_logout(request):
    logout(request)
    return redirect("login")


@cache_control(no_cache=True, must_revalidate=True, no_strore=True)
@login_required(login_url="login")
def ad_post(request):
    if request.method=="POST" and request.FILES:
        movie_title=request.POST['title']
        date_released=request.POST['release_date']
        main_actors=request.POST['actor']
        mov_genre=request.POST['genre']
        trailer=request.POST['trailer']
        upload_movie=request.FILES['upload']
        movie_poster=request.FILES['poster']
        description=request.POST['description']

        post_added.objects.create(
            posted_by=request.user.signin,
            m_title=movie_title,
            m_description=description,
            realese_date=date_released,
            m_flyer=movie_poster,
            m_actors=main_actors,
            m_trailer=trailer,
            movie=upload_movie,
            m_genre=mov_genre,
            posted_date=datetime.datetime.now()
        
        )
    return render(request,"dashboard.html")

@cache_control(no_cache=True, must_revalidate=True, no_strore=True)
@login_required(login_url="login")
def ad_contact(request):
    if request.method=="POST":
        fname=request.POST['fullname']
        mail=request.POST['email']
        text_us=request.POST['subject']

        new_contact=contact(
            names=fname,
            email=mail,
            m_message=text_us
        )
        new_contact.save()

    return render(request,"contact.html",{})

def favorite(request, movie_id,user_id ):
    movie = post_added.objects.get(id = movie_id)
    user = signin.objects.get(id = user_id)
    m_favorite =  favorite_movie(
        movie_title=movie,
        uploader=user
    ) 
    m_favorite.save()
    return redirect('dashboard')






def callindex(response):
    i=post_added.objects.all().order_by("-posted_date")[:3]
    context={'i':i}
    return render(response,'index.html', context)

def callsearch(request):
    if request.method == "POST":
        find = request.POST['find']
        finder = post_added.objects.filter(m_title__icontains = find)
    return render(request, 'search.html', {'results': finder})
def callplay(request,movie_id):
    m_play= post_added.objects.get(id = movie_id)

    return render(request, 'play.html', {'i': m_play})

    return render(request,'play.html',)   
    
def callpost(response):
    return render(response,'post.html',)
def callabout(response):
    return render(response,'about.html',)
def callprofile(response):
    return render(response,'profile.html',)




from django.contrib import admin
from finalproject1.models import signin,post_added,contact,favorite_movie





admin.site.register(signin)
admin.site.register(post_added)
admin.site.register([contact,favorite_movie])




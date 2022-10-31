from django.urls import path
from .views import home ,post,category,signup,signin,signout,sendanemail,contactus, submit
urlpatterns = [
    path('',signin),
    path('home/',home),
    path('blog/<slug:url>',post),
    path('category/<slug:url>',category),
    path('signup',signup),
    path('login/',signin),
    path('logout/',signout),
    path('send/',sendanemail,name="email"),
    path('contactus/',contactus, ),
    path('submit/',submit,name="submit"),
   

   
]

from django.urls import path
from django.contrib import admin

from . import views
from django.contrib.auth.views import LogoutView

from django.contrib import admin
from django.urls import  re_path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'app'
urlpatterns =[
    

   
    path('blog/<id>/', views.detallepost,name='detalle_post'),
    path('',views.inicio,name= 'inicio'),
    path('login/',views.ingreso,name= 'ingreso'),
    path('registro/',views.registro,name='registro'),
    path('sobremi/',views.sobremi,name='sobremi'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('editarperfil/',views.editarperfil,name= 'editarperfil'),
    path('blog/',views.blog, name= 'blog'),
    path('crearblog/',views.crearblog,name= 'crearblog'),
    path('eliminarblog/<id>/',views.eliminarblog,name= 'eliminarblog'),
    path('editarblog/<id>/',views.editarblog,name='editarblog'),
    
 
]

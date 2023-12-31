"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('',index),
    path('tryc/',tryc),
    path('login/',login),
    path('sign/',sign),
    path('check/',check),
    path('mailing/',mailing),
    path('sendmail/',sendmail),
    path('saveuser/',saveuser),
    path('forget/',forget),
    path('getpass/',getpass),
    path('postblog/<str:uid>',postblog),
    path('saveblog/',saveblog),
    path('showblog/<str:uid>',showmyblog),
    path('showmyblog/<str:uid>',showmyblog),
    path('main/',main),
    path('showuser/',showuser),
    path('deleteblog/<str:uid>',deleteblog),
    path('DeleteB/<str:bid>',DeleteB),
    path('showbloguser/<str:bid>/<str:uid>',showbloguser),
    path('blog/<str:uid>',blog),
    path('confg/<str:uid>',confg),
]

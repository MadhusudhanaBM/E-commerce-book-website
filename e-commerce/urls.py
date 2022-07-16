"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,re_path
from hello.views import about, add_order, contact, contact_info, home,greet,hours_ahead,hours_behind,hour_offset,about,contact,contact_info,add_order, model_form_upload, search, simple_upload, visitor
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from hello.views import BookListView,AuthorDetailView,search
from django.contrib.auth import logout, views
from hello.views import register,userlogin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('g/',greet), 
    re_path('now/plus(\d{1,2})hours/',hours_ahead),
    re_path('now/minus(\d{1,2})hours/',hours_behind),
    re_path('now/(plus|minus)(\d{1,2})hours/',hour_offset), 
    path('about/',about),
    path('contact/',contact_info),
    path('add/',add_order),
    path("books/",BookListView.as_view()),
    path('books/author/<int:pk>',AuthorDetailView.as_view()),
    path('',home),
    path('search/',search),
    path('login/',views.LoginView.as_view(), name='login'),
    path('register/',register),
    path('userlogin/',userlogin),
    path('su/',simple_upload),
    path('up/',model_form_upload),
    path('v/',visitor)
    
    

    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

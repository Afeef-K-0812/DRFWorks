"""
URL configuration for movie_crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path,include
from movies import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router=DefaultRouter()
router.register('movies',views.MovieView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('movielist',views.MovieList.as_view()),
    # path('createmovie',views.MovieCreate.as_view()),
    # path('movies',views.MovieListCreate.as_view()),
    # path('movies/<int:pk>',views.MovieRetrieveUpdateDelete.as_view()),
    path('',include(router.urls)),
    path('searchmovies',views.SearchAPIView.as_view()),
    path('userregister',views.RegisterAPIView.as_view()),
    # path('userlogin',views.obtain_auth_token.as_view()),
    path('userlogin',obtain_auth_token)

]

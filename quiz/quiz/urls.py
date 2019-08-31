"""quiz URL Configuration

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
from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth import views as auth_views
from signup import views as signup_views
from createQuiz import views as cq_views
from takeQuiz import views as tq_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url( r'^login/$',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="logged_out.html"), name='logout'),
    url(r'^signup/$', signup_views.signup, name='signup'),
    url(r'^create_quiz/$', cq_views.create_quiz, name='create_quiz'),
    url(r'^quiz_stats/$', cq_views.quiz_stats, name='quiz_stats'),
    url(r'^quiz_list/$', tq_views.quiz_list, name='quiz_list'),
    url(r'attempt_quiz/$', tq_views.attempt_quiz, name='attempt_quiz'),
    path('', include('social_django.urls', namespace='social')),
    url(r'^$', signup_views.home, name='home'),
]

"""hjh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from han import views as hjh_views

urlpatterns = [
    url(r'^makeyou/edit/$', hjh_views.edit_page, name='edit_page'),
    url(r'^makeyou/agreement/$', hjh_views.agree_page, name='agree_page'),
    url(r'^makeyou/$', hjh_views.main_page, name='main_page'),
    url(r'^admin/', admin.site.urls),
]

"""ManageByDjango URL Configuration

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
from django.urls import path, include  # Django2中的语法
# from django.conf.urls import include, url # Django1.11中的语法
import xadmin
urlpatterns = [
    # path('admin/', admin.site.urls),
    # xadmin后台
    path('admin/', xadmin.site.urls),
    #path('v1/users/', include('users.urls')),
]

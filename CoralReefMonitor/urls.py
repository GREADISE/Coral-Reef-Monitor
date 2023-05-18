"""CoralReefMonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import loginApp.views
import mapApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginApp.views.login_check, name='login'),
    path('', loginApp.views.login_check, name='directToLogin'),
    path('signUp/', loginApp.views.sign_up, name='signUp'),
    path('map/', mapApp.views.map, name='map'),
    path('listOfCoralReef/', mapApp.views.listOfCoralReef, name='listOfCoralReef'),
    path('addCoral/', mapApp.views.addCoral, name='addCoral'),
    path('welcome/', loginApp.views.welcome, name='welcome'),
    path('coral-reef/delete/<int:reef_id>/', mapApp.views.delete_coral_reef, name='delete_reef'),
    path('logOut/', loginApp.views.logOut, name='logOut'),
]






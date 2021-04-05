"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from todo_app import views
from accounts import views as accounts_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name="index"),
    # path('add_task', views.addTask, name="add_task"),
    path('delete_all', views.deleteAll, name="delete_all"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('update/<int:id>', views.update, name="update"),
    
    #accounts' urls
    path('', accounts_view.userLogin, name="login"),
    path('register', accounts_view.userRegister, name="register"),
    path('logout', accounts_view.logoutUser, name="logout"),
]

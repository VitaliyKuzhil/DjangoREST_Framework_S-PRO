"""drf_project URL Configuration

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
from django.urls import path, include
from store import views
from store.urls import store_router, user_stores_router, admin_stores_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('today/', views.today, name="today"),
    path('hello_world/', views.hello, name="hello"),
    path('my_name/<str:name_of_hacker>/', views.name, name="name"),
    path('calculator/', views.calculator, name="calculator"),
    path('store/', views.StoreApiView.as_view(), name="store"),
    path('stores/', include(store_router.urls), name="stores"),
    path('my_stores/', include(user_stores_router.urls), name="user_stores"),
    path('admin_stores/', include(admin_stores_router.urls), name="admin_stores")
]

from django.urls import path, include
from rest_framework import routers
from store.views import StoreViewSet, UserStoreViewSet, AdminStoreViewSet

store_router = routers.SimpleRouter()
store_router.register('', StoreViewSet, basename='stores_router')

user_stores_router = routers.SimpleRouter()
user_stores_router.register('', UserStoreViewSet, basename='user_stores_router')

admin_stores_router = routers.SimpleRouter()
admin_stores_router.register('', AdminStoreViewSet, basename='admin_stores_router')

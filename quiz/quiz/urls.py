from django.contrib import admin
from django.urls import path
from accounts.views import get_users, get_user
from products.views import get_products, get_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', get_users, name='get_users'),
    path('users/<int:pk>/', get_user, name='get_user'),
    path('products/', get_products, name='get_products'),
    path('products/<int:pk>/', get_product, name='get_product'),
]

from accounts.views import token_obtain_pair

urlpatterns += [
    path('api/token/', token_obtain_pair, name='token_obtain_pair'),
]

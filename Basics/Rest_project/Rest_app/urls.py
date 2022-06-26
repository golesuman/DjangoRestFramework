from django.urls import path, include
# from .views 
from .import views


urlpatterns = [
    path('products/', views.product_list, name = 'product'), 
    path('products/<int:id>/', views.get_product, name = 'get_product'), 
    # path
    # path('/post'), 
]

from django.urls import path
from .views import (ProductListView, ProductDetailView, 
                    AddToCartView, RemoveFromCartView,
                    CategoryListView)

app_name = 'product'

urlpatterns = [
    path('list/<int:pk>', ProductListView.as_view(), name="list"),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('add/<int:pk>', AddToCartView.as_view(), name='add'),
    path('remove/<int:pk>', RemoveFromCartView.as_view(), name='remove'),
    path('category', CategoryListView.as_view(), name='category_list')
]
from django.db import models
from django.shortcuts import (get_object_or_404, redirect)
from django.views.generic import (ListView, DetailView, View)
from .models import (Product, Category)
from cart.models import Cart

# Create your views here.

class ProductListView(ListView):

    template_name = 'products/product_list.html'

    def get_queryset(self):

        pk = self.kwargs.get('pk')
        category = get_object_or_404(Category, pk=pk)
        queryset = Product.objects.filter(category=category)
        return queryset 



class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'

    def get_objects(self, queryset):

        pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)
        return product


class AddToCartView(View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = request.user
        cart = get_object_or_404(Cart, user=user)
        product = get_object_or_404(Product, pk=pk)
        cart.products.add(product)
        return redirect(f'../detail/{pk}')

class RemoveFromCartView(View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = request.user
        cart = get_object_or_404(Cart, user=user)
        product = get_object_or_404(Product, pk=pk)
        cart.products.remove(product)
        return redirect(request.META.get('HTTP_REFERER', '/'))  
    

class CategoryListView(ListView):

    queryset = Category.objects.all()
    template_name = 'category/category_list.html'

        








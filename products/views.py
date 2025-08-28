from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from django.http import HttpResponse




def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'products/home.html', 
                  {'categories': categories,
                   'products': products 
                   })

#List all categories
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#List products, Filter by category
class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.request.query_params.get('category')
        search = self.request.query__params.get('search')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if search: 
            queryset = queryset.filter(name__incotains=search)
            return queryset
        
#Product details        
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


             




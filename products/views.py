from django.shortcuts import render, get_object_or_404 
from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from django.http import HttpResponse



def home(request):
    categories = Category.objects.all()
    category_id = request.GET.get("category")  # get category from URL
    search = request.GET.get("search")  # get search keyword from URL

    products = Product.objects.all()
    if category_id:
        products = products.filter(category_id=category_id)
    if search:
        products = products.filter(name__icontains=search)

    return render(request, "products/home.html", {
        "categories": categories,
        "products": products,
        "selected_category": int (category_id) if category_id else None, 
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
        search = self.request.query_params.get('search')

        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if search: 
           queryset = queryset.filter(name__icontains=search)

        return queryset
        
#Product details        
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def product_list(request):
    category_id = request.GET.get("category")
    search = request.GET.get("search", "")
    products = Product.objects.all()

    if category_id:
        products = products.filter(category_id=category_id)
    if search:
        products = products.filter(name_icontains=search)

    categories = Category.objects.all()
    return render(request, "products/product_list.html", {
        "products": products,
        "categories": categories,
        "selectef_category": int(category_id) if category_id else None
    })

def product_detail(request, pk): 
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_detail.html", {"product": product})    





             




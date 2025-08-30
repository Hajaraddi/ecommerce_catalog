

from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryListView

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]

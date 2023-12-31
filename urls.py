from .views import BlogCreateView, BlogDeleteView, BlogDetailView, BlogListView, BlogUpdateView
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name="list"),
    path('<int:pk>/', BlogDetailView.as_view(), name="detail"),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name="delete"),
]

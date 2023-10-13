from . import views
from .views import BlogList
from django.urls import path


urlpatterns = [
   path('', views.BlogList.as_view(), name='blogpost'),
   path('add_blogpost/', views.add_blogpost, name='add_blogpost'),
   path('edit_blogpost/<slug:slug>', views.edit_blogpost, name='edit_blogpost'),
   path
   ('delete_blogpost/<slug:slug>', views.delete_blogpost, name='delete_blogpost'),
   path('<slug:slug>/', views.BlogDetail.as_view(), name='blogpost_detail'),
   path('<slug:slug>', views.BlogLike.as_view(), name='blogpost_like'),
]
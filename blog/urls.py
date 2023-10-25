from . import views
from .views import BlogList
from django.urls import path


urlpatterns = [
   path('', views.BlogList.as_view(), name='blogpost'),
   path('<slug:slug>/', views.BlogDetail.as_view(), name='blogpost_detail'),
   path('<slug:slug>', views.BlogLike.as_view(), name='blogpost_like'),
]

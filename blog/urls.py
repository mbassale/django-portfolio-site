from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog'),
    path('<int:post_id>/', views.detail, name='blog_detail')
]

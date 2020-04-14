from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>', views.detail_view, name='post_detail'),
    path('post/new', views.edit_view, name='post_edit'),
]

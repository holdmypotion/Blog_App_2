from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.detail_view, name='post_detail'),
    path('post/new/', views.post_create_view, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit_view, name="post_edit"),
    path('drafts/', views.post_draft_view, name='post_draft_list'),
    path('post/<int:pk>/publish', views.post_publish, name='post_publish'),
]

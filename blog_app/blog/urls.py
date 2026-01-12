from django.urls import path
from .views import home, post_list, create_post, update_post

urlpatterns = [
    path('', home, name='home'),
    path('post_list/', post_list, name='post_list'),
    path('create/', create_post, name='create_post'),
    path('post/<int:post_id>/edit/', update_post, name='update_post')
]

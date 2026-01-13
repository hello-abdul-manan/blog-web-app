from django.urls import path
from .views import home, post_list, create_post, update_post, delete_post, signup_view, login_view, logout_view, post_detail

urlpatterns = [
    path('', home, name='home'),
    path('post_list/', post_list, name='post_list'),
    path('create/', create_post, name='create_post'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/<int:post_id>/edit/', update_post, name='update_post'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

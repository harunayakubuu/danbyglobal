from django.urls import path

from .views import blog_posts, post_details


app_name = "blog"


urlpatterns = [
    path('', blog_posts, name = 'blog-posts'),
    path('post/<str:slug>/', post_details, name = 'blog-details'),
]
from django.urls import path
from .views import home_view, student_login_view, create_post_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', student_login_view, name='student-login'),
    path('create-post/', create_post_view, name='create-post'),
]
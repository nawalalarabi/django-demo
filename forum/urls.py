from django.urls import path
from .views import home, AddPost


urlpatterns = [
    path('', home, name='home'),
    path('post/add/', AddPost.as_view(), name='add_post')
]

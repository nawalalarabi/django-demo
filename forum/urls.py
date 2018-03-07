from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<int:month>/<slug:slug>/', views.PostShow.as_view(), name='post'),
    path('post/add/', views.AddPost.as_view(), name='add_post'),
    path('<int:year>/<int:month>/<slug:slug>/edit/', views.PostEditView.as_view(), name='post_edit')
]

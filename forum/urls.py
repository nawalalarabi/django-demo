from django.urls import path, include
from . import views


api_urls = [
    path('api/posts/', views.PostListAPIView.as_view(), name='post_list_api'),
    path('api/posts/add', views.PostAddAPIView.as_view(), name='post_add_api')
]

urlpatterns = [
    path('', include(api_urls)),
    path('', views.home, name='home'),
    path('<int:year>/<int:month>/<slug:slug>/', views.PostShow.as_view(), name='post'),
    path('post/add/', views.AddPost.as_view(), name='add_post'),
    path('<int:year>/<int:month>/<slug:slug>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('<int:year>/<int:month>/<slug:slug>/delete/', views.PostDelete.as_view(), name='post_delete'),
]

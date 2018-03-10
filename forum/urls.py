from django.urls import path, include
from . import views


api_urls = [
    path('', views.PostListAPIView.as_view(), name='post_list_api'),
    path('add', views.PostAddAPIView.as_view(), name='post_add_api'),
    path('edit/<int:pk>', views.PostEditAPIView.as_view(), name='post_edit_api'),
    path('delete/<int:pk>', views.PostDeleteAPIView.as_view(), name='post_delete_api'),
    path('show/<int:pk>', views.PostShowAPIView.as_view(), name='post_show_api')
]

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<int:month>/<slug:slug>/', views.PostShow.as_view(), name='post'),
    path('post/add/', views.AddPost.as_view(), name='add_post'),
    path('<int:year>/<int:month>/<slug:slug>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('<int:year>/<int:month>/<slug:slug>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('api/posts/', include(api_urls)),
]

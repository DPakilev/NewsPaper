from django.urls import path

from .views import PostCreateView, PostDeleteView, PostDetailView, PostSearchView, PostList, PostUpdateView



urlpatterns = [
    path('', PostList.as_view()),
    path('search/', PostSearchView.as_view(), name='post_search'),
    path('add/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_edit')
]

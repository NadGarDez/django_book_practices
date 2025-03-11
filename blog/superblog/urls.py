from django.urls import path
from .views import HomeView, DetailPage, ListPage, NewPostPage, UpdatePost, DeletePost

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('list_page/', ListPage.as_view(), name= 'list_page'),
    path('post/create/', NewPostPage.as_view(), name='new_post'),
    path('item_page/<int:pk>/',DetailPage.as_view(), name='detail_page'),
    path('post/update/<int:pk>/', UpdatePost.as_view(), name='update_post'),
    path('post/delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),
]

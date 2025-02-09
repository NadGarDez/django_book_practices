from django.urls import path
from .views import HomeView, DetailPage, ListPage

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('list_page/', ListPage.as_view(), name= 'list_page'),
    path('item_page/<int:pk>/',DetailPage.as_view(), name='detail_page')
]

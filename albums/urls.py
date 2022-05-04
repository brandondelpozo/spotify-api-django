from django.urls import path
from .views import AlbumList, AlbumDetail

urlpatterns = [
    path('<int:pk>/', AlbumDetail.as_view()),
    path('', AlbumList.as_view()),
]
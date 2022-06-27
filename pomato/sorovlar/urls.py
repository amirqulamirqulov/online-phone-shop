from django.urls import path
from .views import *
urlpatterns = [
    path('', phone, name = 'phone'),
    path('add', add_phone, name = 'add_phone'),
    path('change/<int:pk>', add_phone, name = 'change'),
    path('delete/<int:pk>', delete_phone, name = 'delete'),
    path('author/', AuthorListView.as_view(), name = 'author'),
    path('author/add', AuthorCreateView.as_view(), name = 'author_add'),
    path('author/change/<int:pk>', AuthorUpdateView.as_view(), name = 'author_change'),
    path('author/delete/<int:pk>', AuthorDeleteView.as_view(), name = 'author_delete'),
]


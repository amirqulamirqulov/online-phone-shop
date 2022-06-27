from django.urls import path, include
from .views import *


urlpatterns = [
    path('test_api_view/', test_api_view),
    path('phone_api_view/<int:pk>/', phone_api_view),
    path('phone_api_view/', PhoneListAPIView.as_view()),
    path('phone_api_view/create/', PhoneCreateAPIView.as_view()),
    path('phone_api_view/update/<int:pk>/', PhoneUpdateAPIView.as_view()),
    path('phone_api_view/delete/<int:pk>/', PhoneDestroyAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
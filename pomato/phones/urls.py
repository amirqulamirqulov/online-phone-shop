from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', index, name = 'index'),
    path('brand', brand, name = 'brand'),
    path('brand/Redmi', PhonesListView.as_view(), name = 'Redmi'),
    path('brand/Samsung', PhonesListView.as_view(), name = 'Samsung'),
    path('brand/Iphone', PhonesListView.as_view(), name = 'Iphone'),
    path('brand/Huawei', PhonesListView.as_view(), name = 'Huawei'),
    path('brand/Honor', PhonesListView.as_view(), name = 'Honor'),
    path('brand/Poco', PhonesListView.as_view(), name = 'Poco'),
    path('contact', contact, name = 'contact'),
    path('administration', admin, name = 'administration'),
    path('admin_brand', cache_page(60)(BrandListView.as_view()),  name = 'admin_brand'),
    path('administration/phone_add', BrandCreateView.as_view(), name = 'phone_add'),
    path('administration/phone_change/<int:pk>', BrandUpdateView.as_view(), name = 'phone_change'),
    path('administration/phone_delete/<int:pk>', BrandDeleteView.as_view(), name = 'phone_delete'),
    path('admin_phone', cache_page(60)(PhoneListView.as_view()), name = 'admin_phone'),
    path('administration/add_phones', PhoneCreateView.as_view(), name = "add_phones"),
    path('administration/update_phones/<int:pk>', PhoneUpdateView.as_view(), name = 'update_phones'),
    path('administration/delete_phones/<int:pk>', PhoneDeleteView.as_view(), name = 'delete_phones'),
    path('register', user_register_view, name = 'register'),
    path('login', user_login_view, name = 'login'),
]
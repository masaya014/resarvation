from django.urls import path
from . import views

app_name = 'booking'


urlpatterns = [
    path('',views.StoreList.as_view(), name='store_list'),
    path('store/<int:pk>/staffs/',views.StaffList.as_view(), name='staff_list'),
]

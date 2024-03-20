from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', views.index, name='home'), 
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item'),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    # path('booking/', views.BookingViewSet.as_view(), name='book')
]
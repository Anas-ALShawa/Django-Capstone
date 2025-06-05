from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)
urlpatterns = [
    path('home', views.home),
    path('api-token-auth/', obtain_auth_token),
    path('restaurant/booking/', include(router.urls)),
    path('menu', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]

from .views import RegisterAPI
from django.urls import path,include
from knox import views as knox_views
from .views import LoginAPI,AccountViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'account', views.AccountViewSet)

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/', include(router.urls))
]

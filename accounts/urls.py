from django.urls import path

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views



app_name = 'accounts'

urlpatterns = [
    path('register/',views.UserRegister.as_view(),name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]


router = routers.SimpleRouter()
router.register('user',views.UserViewSet)
urlpatterns += router.urls 
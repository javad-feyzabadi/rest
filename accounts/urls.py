from django.urls import path

from rest_framework.authtoken import views


from .views import UserRegister

app_name = 'accounts'

urlpatterns = [
    path('register/',UserRegister.as_view(),name='register'),
    path('api-token-auth/', views.obtain_auth_token),

]

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from users.views import AccountLoginAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', AccountLoginAPIView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
    path('api/posts/', include('posts.urls')),
    path('api/users/', include('users.urls')),
]
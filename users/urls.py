from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, UserActivity

router = DefaultRouter()
router.register('', UserViewSet)
urlpatterns = router.urls
urlpatterns.append(path('activity/<int:user_id>/', UserActivity.as_view()))

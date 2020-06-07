from django.urls import path
from .views import PostViewSet, LikeView, UnlikeView, LikeAnalytics
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PostViewSet)
urlpatterns = router.urls
urlpatterns.append(path('<int:post_id>/like/', LikeView.as_view()))
urlpatterns.append(path('<int:post_id>/unlike/', UnlikeView.as_view()))
urlpatterns.append(path('analytics', LikeAnalytics.as_view()))

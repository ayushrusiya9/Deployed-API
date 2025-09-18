from rest_framework import routers
from .views import StudentViewSet
from rest_framework.routers import DefaultRouter


# router = routers.SimpleRouter()
# router.register(r'users', StudentViewSet)
# urlpatterns = router.urls

router = DefaultRouter()
router.register(r'users', StudentViewSet, basename='user')
urlpatterns = router.urls
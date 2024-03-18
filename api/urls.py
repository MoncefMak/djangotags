from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import TagsViewset

router = DefaultRouter()

router.register('tag', TagsViewset, basename="tag")

urlpatterns = router.urls

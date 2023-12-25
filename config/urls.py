from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.views import ExerciseViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register(r'exercises', ExerciseViewSet)
router.register(r'images', ImageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls
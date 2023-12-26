from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.views import ExerciseViewSet

router = routers.DefaultRouter()
router.register(r'exercises', ExerciseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api.views import ExerciseViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="GymBuddy API",
        default_version='v1',
        description="GymBuddy is a powerful yet user-friendly API that empowers developers to build innovative fitness applications. With GymBuddy, you can access a wealth of exercise data to bring your users' fitness goals to life.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="Loma256@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('exercises/', ExerciseViewSet.as_view({'get': 'list', 'post': 'create'}), name='exercise-list-create'),
    path('exercises/<int:pk>/', ExerciseViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='exercise-detail'),
    path('exercises/name/<str:name>/', ExerciseViewSet.as_view({'get': 'list'}), name='exercise-by-name'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

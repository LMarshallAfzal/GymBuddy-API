from django.urls import include, path
from rest_framework import routers
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
    authentication_classes=[]
)

router = routers.DefaultRouter()
router.register(r'exercises', ExerciseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls
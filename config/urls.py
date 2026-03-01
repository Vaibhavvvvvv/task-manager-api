from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from tasks.views import RegisterView, TaskViewSet
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# DRF Router for TaskViewSet
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

# Swagger / OpenAPI Schema
schema_view = get_schema_view(
   openapi.Info(
      title="Task Manager API",
      default_version='v1',
      description="API documentation",
   ),
   public=True,
   permission_classes=(AllowAny,),
   authentication_classes=[],  # JWT will be passed manually via Bearer
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # API Endpoints
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger UI
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
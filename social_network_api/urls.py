from django.contrib import admin
from django.urls import path, include
from posts.api.viewsets import PostsViewSet
from users.api.viewsets import UserViewSet
from users.views import RegisterAPI
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

router = DefaultRouter()
router.register('posts', PostsViewSet, basename='Posts')
router.register('users', UserViewSet, basename='Users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh_pair'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('api/v1/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "iBR Tecnologia"
admin.site.site_title = "Painel Admistrativo"
admin.site.index_title = "Painel iBR"

from django.contrib import admin
from django.urls import path, include
from posts.api.viewsets import PostsViewSet
from users.views import RegisterAPI
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

router = DefaultRouter()
router.register('posts', PostsViewSet, basename='Posts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('api/v1/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "iBR Tecnologia"
admin.site.site_title = "Painel Admistrativo"
admin.site.index_title = "Painel iBR"

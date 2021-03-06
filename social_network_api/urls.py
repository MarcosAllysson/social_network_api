from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from posts.api.viewsets import PostsViewSet
from users.api.viewsets import UserViewSet
from users.views import RegisterAPI
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from users.api.viewsets import MyTokenObtainPairView

router = DefaultRouter()
router.register('posts', PostsViewSet, basename='Posts')
router.register('users', UserViewSet, basename='Users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('api/v1/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "iBR Tecnologia"
admin.site.site_title = "Painel Admistrativo"
admin.site.index_title = "Painel iBR"

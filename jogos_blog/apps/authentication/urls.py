from rest_framework.routers import DefaultRouter
from django.urls.conf import (
    include,
    path
)

from jogos_blog.apps.authentication import views

router = DefaultRouter()

router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
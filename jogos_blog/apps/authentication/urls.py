from django.urls.conf import (
    path
)

from jogos_blog.apps.authentication import views


urlpatterns = [
    path('register/', views.register_user, name="register"),
    path('login/', views.do_login, name="login"),
    path('logout/', views.do_logout, name="logout"),
    path('', views.main, name='main')
]

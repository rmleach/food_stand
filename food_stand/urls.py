
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from register import views as register_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('distros/', include('distros.urls')),
    path('register/', register_views.register, name='register'),
    path('profile/', register_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),
]

if settings.DEBUG:
  urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

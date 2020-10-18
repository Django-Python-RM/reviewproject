from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviewpost.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'),
    ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

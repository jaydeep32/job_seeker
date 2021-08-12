from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('job.urls', namespace='job')),
    path('user/', include('user.urls', namespace='user')),
    path('admin/', admin.site.urls),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path,include
import viewcrud.urls
import viewcrud.views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',viewcrud.views.welcome,name='welcome'),
    path('funccrud/', include(viewcrud.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


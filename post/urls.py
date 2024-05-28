from django.urls import path
from django.contrib import admin
from .views import write, detail
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name='post'

urlpatterns = [
    path('write/', write, name='write'),
    path('<int:id>/', detail, name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
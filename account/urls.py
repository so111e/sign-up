from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('<str:username>/', home, name='home'),
    path('signup/', signup, name='signup'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
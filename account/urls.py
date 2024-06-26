from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('<str:username>/', home, name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
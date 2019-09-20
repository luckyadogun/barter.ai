from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('feeds/', views.feeds, name='feeds'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-pitch/', views.create_pitch, name='create-pitch'),
    path('add-portfolio/', views.add_portfolio, name='add-portfolio'),
    path('me/messages/', views.my_messages, name='my-messages'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
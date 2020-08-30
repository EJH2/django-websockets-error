from django.urls import path

from tasks import views

urlpatterns = [
    path('ws', views.ws_view, name='ws'),
    path('ws_error', views.ws_error_view, name='ws_error'),
    path('', views.index, name='index')
]

from django.urls import path
from . import views

app_name = 'libraries'
urlpatterns = [
    path('', views.index, name='index'), # /libraries/
    path('<int:pk>', views.detail, name='detail') # /libraries/1/
]

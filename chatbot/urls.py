
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.chat_view , name= 'index')
    # path('', views.index, name='index'),
    # path('get-gemini-response/', views.get_gemini_response, name='get_gemini_response'),
]
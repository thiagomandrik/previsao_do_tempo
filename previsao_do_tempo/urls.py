
from django.urls import path, include
from previsao_do_tempo.views import index

urlpatterns = [
    path('', index, name="index")
]

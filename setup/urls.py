from django.contrib import admin
from django.urls import path, include

import previsao_do_tempo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('previsao_do_tempo.urls'))
]

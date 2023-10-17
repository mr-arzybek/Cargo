
from django.contrib import admin
from django.urls import path , include
from .yasg import urlpatterns_swagger as urls_swagger
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('cargo_app.urls'))

] + urls_swagger

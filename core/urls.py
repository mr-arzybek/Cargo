
from django.contrib import admin
from django.urls import path , include
from .yasg import urlpatterns_swagger as urls_swagger
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.cargo_app.urls')),
    path('api/v1/users/', include('api.users.urls'))


] + urls_swagger

from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Book Operations API EndPoints')

urlpatterns = [
    path('admin/', admin.site.urls),
    url('v1/',include('bookapp.urls')), # modelviewset
    url(r'swagger/', schema_view),#swagger
    url(r'^apiuris/', include('rest_framework.urls')) #rest api
]

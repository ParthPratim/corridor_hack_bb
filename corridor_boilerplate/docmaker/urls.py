from rest_framework.routers import DefaultRouter
from docmaker.views import ModelDocGenerator
from django.urls  import path, include

router = DefaultRouter()
router.register(r'doctool', ModelDocGenerator, basename='doctool')


urlpatterns = [
    path('',include(router.urls)) 
]


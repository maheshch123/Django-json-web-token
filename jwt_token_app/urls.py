from django.urls import path,include
from . import views
from .views import SchoolApi,libraryApi
from rest_framework.routers import DefaultRouter


# from .views import UserView,Userdetails,Detailstodo


router = DefaultRouter()
router.register('schoolApi',SchoolApi)
router.register('libraryapi',libraryApi)

urlpatterns = [
    path('',include(router.urls)),
    
]
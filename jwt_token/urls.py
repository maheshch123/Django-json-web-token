"""jwt_token URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('jwt_token_app.urls')), 
    path('docs/',include_docs_urls(title='School APi')), # for documentation
    path('api/jwt/token',jwt_views.TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('api/jwt/token/refresh',jwt_views.TokenRefreshView.as_view(),name="token_refresh"),

]


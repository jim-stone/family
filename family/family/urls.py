"""
URL configuration for family project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from main.api import (FamilyViewset, AsessmentViewset,
                      LoginView, LogoutView, UserViewset,
                      WishReadViewset, WishWriteViewset)
from main.views import IndexView, FamiliesView, OpinionsView, WishesView

router = routers.DefaultRouter()
router.register(r'families', FamilyViewset)
router.register(r'opinions', AsessmentViewset)
router.register(r'users', UserViewset)
router.register(r'wishes', WishReadViewset)
router.register(r'wishes_write', WishWriteViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('', IndexView.as_view()),
    path('login/', LoginView.as_view()),
    path('api/logout/', LogoutView.as_view()),
    path('index/', IndexView.as_view()),
    path('families/', FamiliesView.as_view()),
    path('opinions/<int:pk>/', OpinionsView.as_view()),
    path('wishes/<int:pk>/', WishesView.as_view()),

]

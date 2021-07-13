from django.urls import path,include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [path("fileUpload", views.index, name="index"),
               path("show", views.show, name="show"),
               path("showAPI", views.showAPIVal, name="showAPIV"),
               path("apiCall", views.apiCall, name="ShowAPI"),
               path('', TemplateView.as_view(template_name="index.html")),
               path('accounts/', include('allauth.urls')),
               path('logout', LogoutView.as_view()),
               ]

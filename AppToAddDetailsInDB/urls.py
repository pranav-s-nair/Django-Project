from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
               path("/show", views.show, name="show"),
               path("/ShowAPI", views.showAPIVal, name="showAPIV"),
               path("/APICall", views.apiCall, name="ShowAPI")]

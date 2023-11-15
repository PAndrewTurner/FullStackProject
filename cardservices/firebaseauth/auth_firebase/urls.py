from django.urls import path
from . import views

urlspatterns = [
    path("api/students/", views.StudentAPIView.as_view(), name="api-student"),
  ]

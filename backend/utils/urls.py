from django.urls import include, path
from . import views


urlpatterns = [
path("api/rest_test", views.rest_test.as_view(), name="rest_test"),
]
from django.urls import path
from .views import individual

urlpatterns = [
    path("", individual, name="individual"),
]

# path("individual/", views.individual, name="individual"),
# http://127.0.0.1:8000/individual/
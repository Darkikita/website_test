from django.urls import path
from .views import site_view, start

urlpatterns = [
    path("", start, name="start"),
    path("<slug:slug>/", site_view, name="site-view"),
]


# from .views import start, individual

# urlpatterns = [
#     path("", start, name="start"),
#     path("individual/", individual, name="individual"),
# ]

# path("individual/", views.individual, name="individual"),
# http://127.0.0.1:8000/individual/
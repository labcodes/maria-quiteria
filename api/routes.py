from api.views import CityCouncilAgendaView, HealthCheckView
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path("", HealthCheckView.as_view()),
    path(
        "city-council-agenda/",
        CityCouncilAgendaView.as_view(),
        name="city-council-agenda",
    ),
]
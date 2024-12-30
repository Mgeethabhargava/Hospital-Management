from django.urls import path
from .views import AppointmentView, AnalyticsView

urlpatterns = [
    path('appointments/', AppointmentView.as_view(), name='appointments'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
]

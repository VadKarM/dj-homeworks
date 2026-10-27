from django.urls import path

from . import views

urlpatterns = [
    path('sensors/', views.SensorListView.as_view(), name='sensor-list'),
    path('sensors/<int:pk>/', views.SensorDetailView.as_view(), name='sensor-detail'),
    path('measurements/', views.MeasurementCreateView.as_view(), name='measurement-create'),
]

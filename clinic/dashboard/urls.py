from django.conf.urls import url
from django.urls import path


from .views import dashboard, profile_edit, doctor, appointment, calendar, profile, app_cal, check_hours, \
    CreateAppointmentView, medical_history

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('profile_edit/', profile_edit, name='profile_edit'),
    path('doctors/', doctor, name='doctor'),
    path('appointments/', appointment, name='appointment'),
    path('calendar/', CreateAppointmentView.as_view(), name='calendar'),
    path('medical_history/', medical_history, name='medical_history'),
    url('calendar/hours/', check_hours, name='check_hours'),
]
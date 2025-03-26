from django.urls import path
from .views import RegistrationAPIView, AuthAPIView, ConfirmUserAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('authorization/', AuthAPIView.as_view()),
    path('confirm/', ConfirmUserAPIView.as_view()),
]
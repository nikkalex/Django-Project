#feedback_app/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('feedback/',views.feedback,name='feedback'),
    path('feedback_success/',views.feedback_success,name='feedback_success'),
]
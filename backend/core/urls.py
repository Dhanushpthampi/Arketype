
from django.urls import path, include  

from .views import health, get_questions,submit_answers
urlpatterns = [
    path('health/', health),
    path('questions/', get_questions),
    path('submit/',submit_answers),
]

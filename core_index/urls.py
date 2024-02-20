from django.urls import path
from core_index.views import *

urlpatterns = [
    path('', index),
]

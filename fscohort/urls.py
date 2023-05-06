from django.urls import path
from .views import fscohort,goodbye

urlpatterns = [
    path('', fscohort),
    path('goodbye/', goodbye)
]
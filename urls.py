from django.urls import path
from . import views

urlpatterns = [
    path('download/<str:id>', views.download),
    path('scrape/<path:url>', views.scrape),
]

from invalid import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('inflex/',views.inflex)
]

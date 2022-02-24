from django.urls import path

from . import views
from .views import HomeView, FlockView, FeedView, CoupeDayView, FlockUpdateView, FlockDeleteView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('flocks/', FlockView.as_view(), name='flocks'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('frecords/', CoupeDayView.as_view(), name='records'),
    path('egg_per_day/', views.egg_chart, name='egg_chart'),
    path('flocks/<int:pk>/', FlockUpdateView.as_view(), name='flock-update'),
    path('flocks/<int:pk>/delete/', FlockDeleteView.as_view(), name='flock-delete'),
]
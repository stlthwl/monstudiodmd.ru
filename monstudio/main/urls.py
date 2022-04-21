from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('team', views.team, name='team'),
    path('about', views.about, name='about'),
    path('reviews', views.reviews, name='reviews'),
    path('makeReview', views.makereview, name='makeReview'),
]
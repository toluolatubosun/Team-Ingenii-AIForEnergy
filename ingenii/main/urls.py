from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('about-solution/', views.OurSolution, name='Our Solution'),
    path('feature-selection/', views.FeatureSelection, name='Feature Selection'),
    path('prediction-suggestion/', views.PredictionSuggestion, name='Prediction & Suggestion'),
    path('result/', views.Result, name='Result'),
]


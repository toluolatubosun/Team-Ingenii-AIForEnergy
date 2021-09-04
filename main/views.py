from django.shortcuts import render, redirect
from django.http import HttpResponse
from modules.predict_suggest import predict_suggest

def Home(response):
    return render(response, "main/home.html", {"name": "Home"})

def OurSolution(response):
    return render(response, "main/our-solution.html", {"name": "Our Solution"})

def FeatureSelection(response):
    return render(response, "main/feature-selection.html", {"name": "Feature Selection"})

def PredictionSuggestion(response):
    return render(response, "main/prediction-suggestion.html", {"name": "Prediction & Suggestion"})

def Result(response):
    if response.method == "POST":
        data = predict_suggest(response.POST)
        return render(response, "main/result.html", {"name": "Result", "data": data})
    else:
        return redirect('/', {"name": "Home"})

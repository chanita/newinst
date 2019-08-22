from django.shortcuts import render

def home(request):
    more_context = {"greeting": "สวัสดี"}
    more_context["best_price"] = 3000.00
    return render(request, "home/home.html", more_context)

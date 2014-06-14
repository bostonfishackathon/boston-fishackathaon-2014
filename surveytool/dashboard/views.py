from django.http import HttpResponse
from django.shortcuts import render

def dashboard(request):
    context = {}
    return render(request, 'dashboard/dashboard.html', context)


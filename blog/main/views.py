from django.shortcuts import render
import datetime
# Create your views here.

def main(request):
    context = {'like': 'Django 很棒', 'now': datetime.datetime.now()}
    return render(request, 'main/main.html', context)

def about(request):
    return render(request, 'main/about.html')
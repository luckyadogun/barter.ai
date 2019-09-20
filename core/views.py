from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from triibe_project.settings import FORM_ERROR_MESSAGE

from core.models import Entrepreneur, Pitch

def index(request):
    if request.user.is_authenticated:
        return redirect('core:feeds')
    return render(request, 'core/index.html', {})

#add account status - active, inactive

#check if entrepreneur account has been updated to create feed or connect
#modal has button to take them to account update
def feeds(request):
    entrp = get_object_or_404(Entrepreneur, user_id=request.user.id)
    pitches = Pitch.objects.all()
    data = {'entrepreneur': entrp, 'pitches': pitches}
    return render(request, 'core/feeds.html', data)

def dashboard(request):
    entrp = get_object_or_404(Entrepreneur, user_id=request.user.id)
    return render(request, 'core/dashboard.html', {'entrepreneur': entrp})

def create_pitch(request):
    #TODO:
    # Clean up code
    # Write Test
    # Rename Project
    # Design CI/CD pipeline

    entrp = get_object_or_404(Entrepreneur, user_id=request.user.id)
    if request.method == 'POST':
        pitch = Pitch(
            title=request.POST.get('title'),
            body=request.POST.get('content'),
            skills=request.POST.get('skills'),
            offer_status=request.POST.get('offer_status'))
        pitch.entrepreneur = entrp
        pitch.save()
        messages.success(request, "You have successfully created a pitch!")

    data = {'entrepreneur': entrp}
    return render(request, 'core/create_pitch.html', data)

def add_portfolio(request):
    entrp = get_object_or_404(Entrepreneur, user_id=request.user.id)
    return render(request, 'core/add_portfolio.html', {'entrepreneur': entrp})

# def my_pitches(request):
#     entrp = get_object_or_404(Entrepreneur, user_id=request.user.id)
#     return render(request, 'core/my_pitch.html', {'entrepreneur': entrp})

def my_messages(request):
    return render(request, 'core/messages.html', {})
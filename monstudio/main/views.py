from django.shortcuts import render, redirect
from .models import feedback
from .forms import feedbackForm, messageForm


def index(request):
    error = ''
    if request.method == 'POST':
        form = messageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверной'
    form = messageForm()
    context_index = {
        'form': form,
        'error': error
    }
    return render(request, 'main/index.html', context_index)


def team(request):
    return render(request, 'main/team.html')


def about(request):
    return render(request, 'main/about.html')


def reviews(request):
    review = feedback.objects.order_by('-id')
    return render(request, 'main/reviews.html', {'review': review})


def makereview(request):
    error = ''
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
        else:
            error = 'Форма была неверной'
    form = feedbackForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/makeReview.html', context)


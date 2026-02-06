from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.


def HomeView(request):
    context = {'message': "Welcome to the school of schools"}
    return render(request, "home.html", context)

def school_list(request):
    schools = School.objects.all()
    context = {'schools' : schools}
    return render(request, 'school.html', context)


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if Subscriber.objects.filter(email = email).exists():
            messages.error(request, 'OOPS you are already subscribed')
        else:
            subscriber = Subscriber(email = email)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing')
            return redirect('subscribe')
    return render(request, 'subscribe.html')

def add_school(request):
    if request.method == 'POST':
        form = schoolForm(request.POST)
        if form.is_valid():
            school =form.save()
            return redirect('schools')
    else:
        form = schoolForm()
    return render(request, 'add_school.html', {'form': form})
        
def add_teacher(request):  
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            teacher =form.save()
            teacher.save()
    else:
        form = TeacherForm()
    return render(request, 'add_teacher.html', {'form': form})

def teacher_list(request):
    teachers = Teacher.objects.all()
    context = {'teachers' : teachers}
    return render(request, 'teacher.html', context)

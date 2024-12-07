
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from .models import Judge, Audition, Performance
from .forms import PerformanceForm, AuditionForm
from django.contrib import messages

def audition_list(request):
    auditions = Audition.objects.all()
    return render(request, 'judge/audition_list.html', {'auditions': auditions})

def performance_list(request):
    performances = Performance.objects.all()
    return render(request, 'judge/performance_list.html', {'performances': performances})

def rate_performance(request, audition_id):
    audition = Audition.objects.get(id=audition_id)
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Performance rated successfully.")
            return redirect('performance-list')
    else:
        form = PerformanceForm(initial={'audition': audition})
    
    return render(request, 'judge/rate_performance.html', {'form': form, 'audition': audition})

def judge_home(request):
    return render(request, 'judge/home.html')

def create_audition(request):
    if request.method == 'POST':
        form = AuditionForm(request.POST)
        if form.is_valid():
            audition = form.save(commit=False)
            audition.judge = Judge.objects.first() 
            audition.save()
            messages.success(request, "Audition created successfully.")
            return redirect('audition-list')
    else:
        form = AuditionForm()
    
    return render(request, 'judge/create_audition.html', {'form': form})

def delete_audition(request, audition_id):
    audition = get_object_or_404(Audition, id=audition_id)
    audition.delete()
    messages.success(request, "Audition deleted successfully.")
    return redirect('audition-list')

@require_http_methods(["GET"])
def get_all_judges(request):
    judges = Judge.objects.all().values()
    judges_list = list(judges)
    return JsonResponse({"judges": judges_list}, status=200)

@require_http_methods(["GET"])
def get_all_performances(request):
    performances = Performance.objects.all().values()
    performances_list = list(performances)
    return JsonResponse({"performances": performances_list}, status=200)

@require_http_methods(["GET"])
def get_all_auditions(request):
    auditions = Audition.objects.all().values()
    auditions_list = list(auditions)
    return JsonResponse({"auditions": auditions_list}, status=200)
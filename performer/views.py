

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from judge.models import Audition
from performer.models import Performer
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

def performer_home(request):
    return render(request, 'performer/home.html')  


def auditions_list(request):
    auditions = Audition.objects.all()
    return render(request, 'performer/audition_list.html', {'auditions': auditions})

def join_audition(request, audition_id):
    audition = get_object_or_404(Audition, id=audition_id)

 
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'performer':
        messages.error(request, "Only performers can join auditions.")
        return redirect('audition-list')

   
    performer = request.user.profile
    if audition.performance_set.filter(performer=performer).exists():
        messages.error(request, "You have already joined this audition.")
    else:
        
        audition.performance_set.create(performer=performer)
        messages.success(request, f"You have successfully joined the audition: {audition.title}")

    return redirect('audition-list')

@require_http_methods(["GET"])
def get_all_performers(request):
    performers = Performer.objects.all().values()
    performers_list = list(performers)
    return JsonResponse({"performers": performers_list}, status=200)
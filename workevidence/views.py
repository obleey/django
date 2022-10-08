
import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from workevidence.forms import WorkerForm, EvidenceForm
from workevidence.models import WorkEvidence, Worker
from django.contrib.auth.decorators import login_required
from .filters import WorkEvidenceFilter

from .forms import WorkerForm


# Create your views here.

@login_required
def default(request):
    return render(request, 'index.html', {})
  

def workers(request):
    context = Worker.objects.all()

    return render(request, 'worker.html', {'workers':context})

def workerDetails(request,pk):
    worker = get_object_or_404(Worker, pk=pk)
    return render(request, 'worker_detail.html', {'worker': worker})

def addWorker(request):
    form = WorkerForm()
    if request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workers')
    else:
        form = WorkerForm()
    return render(request, 'worker_new.html', {'form': form})


def updateWorker(request, pk):
    worker = Worker.objects.get(id=pk)
    form = WorkerForm(instance=worker)
    if request.method == "POST":
        form = WorkerForm(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            return redirect('workers')
    return render(request, 'worker_new.html', {'form' : form})

def evidence(request):
    context = WorkEvidence.objects.order_by('created_date') 
    evidenceFilter = WorkEvidenceFilter(request.GET, queryset=context)
    context = evidenceFilter.qs
    return render(request, 'evidence.html', {'evidence': context, 'evidence_filter': evidenceFilter})


def addEvidence(request):
    form = EvidenceForm()
    if request.method == "POST":
        form = EvidenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evidence')
    else:
        form = EvidenceForm()
    return render(request, 'evidence_new.html', {'form': form})


def updateEvidence(request, pk):
    worker = WorkEvidence.objects.get(id=pk)
    form = EvidenceForm(instance=evidence)
    if request.method == "POST":
        form = EvidenceForm(request.POST, instance=evidence)
        if form.is_valid():
            form.save()
            return redirect('evidence')
    return render(request, 'evidence_new.html', {'form' : form})



def evidenceDetails(request,pk):
    evidence = get_object_or_404(WorkEvidence, pk=pk)
    return render(request, 'evidence_detail.html', {'evidence': evidence})

   
def celery(request):
    today = datetime.datetime.now()
    today_workers = Worker.objects.filter(created_date__date=today)
    return HttpResponse(today_workers)
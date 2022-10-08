from django.urls import path, include
from . import views
from django.contrib import auth as auth_views
from django.urls import path, include


urlpatterns = [
    path('', views.default, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('worker', views.workers, name='workers'),
    path('worker/<int:pk>', views.workerDetails, name='worker_detail'),
    path('worker/new/', views.addWorker, name='worker_new'),
    path('worker/update/<int:pk>', views.updateWorker, name='worker_update'),
    path('evidence', views.evidence, name='evidence'),
    path('evidence/<int:pk>', views.evidenceDetails, name='evidence_detail'),
    path('evidence/new/', views.addEvidence, name='evidence_new'),
    path('evidence/update/<int:pk>', views.updateEvidence, name='evidence_update'),
]
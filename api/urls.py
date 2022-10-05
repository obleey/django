from django.urls import path
from . import views

urlpatterns = [
    path('',views.getDefaults),
    path('worker/get',views.getUsers),
    path('worker/get/<str:pk>',views.getUserDetail),
    path('worker/add', views.addUser),
    path('evidence/get',views.getEvidence),
    path('evidence/get/<str:pk>',views.getEvidenceDetail),
    path('evidence/add',views.addEvidence)
]
from rest_framework.response import Response
from rest_framework.decorators import api_view
from workevidence.models import Worker, WorkEvidence
from .serializers import WorkerSerializer,EvidenceSerializer


@api_view(['GET'])
def getDefaults(request):
    api_urls =  {
        'Worker': {
              'GET': '/worker/get',
              'GET single': '/worker/get/<str:pk>',
              'POST': '/worker/add',
        },
        'Evidence': {
              'GET': '/evidence/get',
              'GET single': '/evidence/get/<str:pk>',              
              'POST': '/evidence/add',
        },
    }
    return Response(api_urls)

@api_view(['GET'])
def getUsers(request):
    items = Worker.objects.all()
    serializer = WorkerSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUserDetail(request,pk):
    items = Worker.objects.get(id=pk)
    serializer = WorkerSerializer(items, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addUser(request):
    serializer = WorkerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def getEvidence(request):
    items = WorkEvidence.objects.all()
    serializer = EvidenceSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEvidenceDetail(request,pk):
    items = WorkEvidence.objects.get(id=pk)
    serializer = EvidenceSerializer(items, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addEvidence(request):
    serializer = EvidenceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

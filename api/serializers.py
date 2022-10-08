from django.utils import timezone
from rest_framework import serializers
from workevidence.models import Worker, WorkEvidence

class WorkerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(required=True)
    card_id = serializers.CharField(required=True)


    class Meta:
        model = Worker
        fields = '__all__'
    
class EvidenceSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField()
    end_date= serializers.DateTimeField()
    worker = serializers.CharField(required=True)
    class Meta:
        model = WorkEvidence
        fields = '__all__'
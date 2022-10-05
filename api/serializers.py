from rest_framework import serializers
from workevidence.models import Worker, WorkEvidence

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkEvidence
        fields = '__all__'
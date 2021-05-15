from rest_framework import generics
from . import models
from . import serializers


class RemoteworkEvalListView(generics.ListCreateAPIView):
    queryset = models.RemoteworkEval.objects.all()
    serializer_class = serializers.RemoteworkEvalSeriailzer
    

class RemoteworkEvalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.RemoteworkEval.objects.all()
    serializer_class = serializers.RemoteworkEvalSeriailzer
    

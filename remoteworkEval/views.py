from rest_framework import generics
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import status


class RemoteworkEvalListView(generics.ListCreateAPIView):
    queryset = models.RemoteworkEval.objects.all()
    serializer_class = serializers.RemoteworkEvalSeriailzer
    
    def post(self, request, format=None):
        serializer = serializers.RemoteworkEvalSeriailzer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            obj.user = request.user
            obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class RemoteworkEvalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.RemoteworkEval.objects.all()
    serializer_class = serializers.RemoteworkEvalSeriailzer
    

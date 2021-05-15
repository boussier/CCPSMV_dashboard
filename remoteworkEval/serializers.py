from rest_framework import serializers
from .models import RemoteworkEval


class RemoteworkEvalSeriailzer(serializers.ModelSerializer):
    class Meta:
        model = RemoteworkEval
        fields = '__all__'

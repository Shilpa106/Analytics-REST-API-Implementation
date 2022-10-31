from rest_framework import serializers
from fliter_api.models import Filter_data


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class SaveFileSerializer(serializers.Serializer):
    class Meta:
        model = Filter_data
        fields = "__all__"
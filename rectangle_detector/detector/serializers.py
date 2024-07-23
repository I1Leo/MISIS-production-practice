from rest_framework import serializers


class ImagePathSerializer(serializers.Serializer):
    image_path = serializers.CharField()

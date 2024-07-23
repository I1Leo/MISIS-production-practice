from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import ImagePathSerializer
from .utils import find_rectangle_corners
import os


class RectangleDetectView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ImagePathSerializer(data=request.data)
        if serializer.is_valid():
            image_path = serializer.validated_data['image_path']
            if not os.path.exists(image_path):
                return Response({"error": "File not found."}, status=status.HTTP_400_BAD_REQUEST)
            points = find_rectangle_corners(image_path)
            return Response({"points_of_interest": points}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

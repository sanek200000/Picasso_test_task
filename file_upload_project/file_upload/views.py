from rest_framework import generics

from .models import File
from .serializers import FileSerializer


class FileUploadView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
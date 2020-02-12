from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer
from .models import File
from django.conf import settings
import os



class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request):
        """
        Upload a new egg
        """
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        """
        delete an egg
        """
        try:
            del_rec = File.objects.get(pk=pk)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        os.remove(os.path.join(settings.MEDIA_ROOT, str(del_rec.file)))
        del_rec.delete()
        return Response(status=status.HTTP_200_OK)

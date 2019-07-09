
from rest_framework.views import APIView
from rest_framework.mixins import (CreateModelMixin,
                                   DestroyModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.generics import (
                                      ListAPIView,
                                      RetrieveAPIView,
                                      UpdateAPIView,
                                      DestroyAPIView,
                                      CreateAPIView)
from rest_framework.response import Response

from DRFS.models import Status
from .serializers import StatusSerializer
from DRFS.forms import StatusForm


# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#
#     def get(self, request, format = None):
#         qs = Status.objects.all()
#         serialized_data = StatusSerializer(qs, many = True)
#         return Response(serialized_data.data)
#
#
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



##Using Mixins
class StatusListAPIView(CreateModelMixin,ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



# class StatusCreateAPIView(CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


class StatusDetailAPIView(UpdateModelMixin,DestroyModelMixin,RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StatusUpdateAPIView(UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusDeleteAPIView(DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

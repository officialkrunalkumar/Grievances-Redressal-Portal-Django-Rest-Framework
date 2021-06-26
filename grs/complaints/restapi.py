from rest_framework import viewsets
from .serializer import ComplaintSerializer
from .models import Complaint
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import (TokenAuthentication,
                                           BasicAuthentication)
from rest_framework.permissions import IsAuthenticated


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()
    authentication_classes = (BasicAuthentication, TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('due_date').first()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

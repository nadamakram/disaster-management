from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from disasters.models import Disaster, GeoJSON
from disasters.permissions import IsOwnerOrReadOnly
from disasters.serializers import DisasterSerializer
from rest_framework.response import Response


class DisasterViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    serializer_class = DisasterSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    def get_queryset(self):


        disasters = Disaster.objects.all()
        

        return disasters


    def perform_create(self, serializer):
        lat = self.request.data.get("lat")
        lang = self.request.data.get("lang")
        center_point = {
            "type"          :   "Point",
            "coordinates"   :   [lat, lang]  
        }
        point = GeoJSON(**center_point)
        serializer.save(owner=self.request.user, center_point = point)
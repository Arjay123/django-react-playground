from sample.models import Person
from sample.serializers import PersonSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from sample.serializers import UserSerializer
from rest_framework import permissions
from sample.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import viewsets
from rest_framework.decorators import detail_route

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "users": reverse('user-list', request=request, format=format),
        "persons": reverse('person-list', request=request, format=format)
    })



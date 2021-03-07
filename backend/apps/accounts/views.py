from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED
from rest_framework.viewsets import ModelViewSet

from . import serializers

User = get_user_model()


class MeViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]

    @action(methods=['patch'], detail=False)
    def upgrade(self, request):
        self.request.user.is_confirmed = True
        self.request.user.save()
        return Response({"success": "Successfully upgraded to premium!"}, status=HTTP_202_ACCEPTED)

    @action(methods=['patch'], detail=False)
    def downgrade(self, request):
        self.request.user.is_confirmed = False
        self.request.user.save()
        return Response({"success": "Successfully downgraded!"}, status=HTTP_202_ACCEPTED)

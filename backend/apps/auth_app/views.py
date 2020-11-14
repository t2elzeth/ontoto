from django.shortcuts import render

# Create your views here.
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class RestrictedView(APIView):
    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request, *args, **kwargs):
        message = 'Only for logged in users'
        return Response(data=message, status=status.HTTP_200_OK)


class SignupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/signup.html')

    def post(self, request, *args, **kwargs):
        pass


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/login.html')

    def post(self, request, *args, **kwargs):
        pass


class Logout(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/logout.html')

    def post(self, request, *args, **kwargs):
        pass

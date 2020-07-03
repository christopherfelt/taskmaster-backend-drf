from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class Posts(APIView):
    def get(self, request):
        return JsonResponse({"Success":True})
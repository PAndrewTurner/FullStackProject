from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student
from rest_framework.permissions import IsAuthenticated
from auth_firebase.authentication import FirebaseAuthentication

class StudentAPIView(APIView):

    """This api will handle student"""
    permission_classes = [ IsAuthenticated ]

    """Here just add FirebaseAuthentication class in authentication_classes"""
    authentication_classes = [ FirebaseAuthentication ]

    def get(self,request):
            data = Student.objects.all()
            serializer = StudentSerializer(data, many = True)
            response = {
                   "status": status.HTTP_200_OK,
                   "message": "success",
                   "data": serializer.data
                   }
            return Response(response, status = status.HTTP_200_OK)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializer import StudentSerializer
from django.contrib.auth.models import User
  
class HelloView(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)
class StudentCRUD(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self,request):
        user=User.objects.get(username=request.user)
        data=Student.objects.filter(owner=user)
        serializer=StudentSerializer(data,many=True)
        return Response(serializer.data)
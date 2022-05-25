# from .models import Driver, Manager, Vehicle
# from .serializers import DriverRegistartionSerializer, DriverSerializer, ManagerSerializer, VehicleSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import status
# # Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from accounts.models import CustomUser, Driver
from accounts.serializers import DriverRegistrationSerializer, DriverSerializer, UserLoginSerializer, UserProfileSerializer, UserRegistrationSerializer


from rest_framework_simplejwt.tokens import RefreshToken 
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class HelloView(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)

class UserView(APIView):

    permission_classes = (IsAuthenticated, )
    def get(self,request):
        queryset = CustomUser.objects.all()
        serializer = UserProfileSerializer(queryset,many=True)
        return Response(serializer.data)


class DriverView(APIView):

    def get(self,request):
        queryset = Driver.objects.all()
        serializer = DriverSerializer(queryset,many = True)
        return Response(serializer.data)

class UserRegistrationView(APIView):
    def post(self,request,format=None):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Registration successfully Done'})
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class DriverRegistrationView(APIView):
    def post(self,request,format=None):
        serializer = DriverRegistrationSerializer(data = request.data)
        if request.user.type=='Head':
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'msg':'Registration successfully Done'})
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg':'you are not eligible to add driver login as Head'})


class UserLoginView(APIView):
    def post(self,request,format=None):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login Success'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



# class DriverView(APIView):

#     def get(self,request, format = None):
#         queryset = Driver.objects.all()
#         serializer = DriverSerializer(queryset,many=True)
#         return Response(serializer.data)

#     # def post(self,request, format = None):
#     #     serializer = DriverSerializer(data = request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data)
#     #     return Response(serializer.errors,status = status.HTTP_404_NOT_FOUND)


# class DriverRegistrationView(APIView):
    
#     def post(self,request,format=None):
#         serializer = DriverRegistartionSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Registration Done'})
#         return Response(serializer.errors,status = status.HTTP_404_NOT_FOUND)

# class VehiclesView(APIView):

#     def get(self,request,format=None):
#         queryset = Vehicle.objects.all()
#         serializer = VehicleSerializer(queryset,many=True)
#         return Response(serializer.data)
    
#     def post(self,request, format = None):
#         serializer = VehicleSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status = status.HTTP_404_NOT_FOUND)


# class ManagerView(APIView):

#     def get(self,request,format=None):
#         queryset = Manager.objects.all()
#         serializer = ManagerSerializer(queryset,many=True)
#         return Response(serializer.data)
    
#     def post(self,request, format = None):
#         serializer = ManagerSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status = status.HTTP_404_NOT_FOUND)
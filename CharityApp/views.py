from rest_framework import viewsets
from .models import UserModel
from .serializers import UserSerializer, Login_Serializer, Varify_User_Serializer, TransactionSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .emails import *
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class RegisterViewset(viewsets.ViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer 
    http_method_names = ['get', 'post', 'delete']

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            otp = generateOTP()
            request.session['otp']=otp
            email = serializer.validated_data['email']
            request.session['email']=email
            send_email(serializer.validated_data['name'], email, serializer.validated_data['phone_number'], otp)
            user = UserModel.objects.get(email = serializer.data['email'])
            return Response({'data':serializer.data,
                            'status':status.HTTP_201_CREATED, 
                            'messege':'registered successfully'})
        return Response({'status':status.HTTP_400_BAD_REQUEST})


class LoginView(viewsets.ViewSet):
    queryset = UserModel.objects.all()
    serializer_class = Login_Serializer

    def create(self, request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            email=serializer.data['email']
            password=serializer.data['password']
            email = email.lower()
            user_data = UserModel.objects.filter(email=email).first()
            user=authenticate(email=email, password=password)
            print(user)

            if user is None:
                return Response({
                            'status':status.HTTP_400_BAD_REQUEST,
                            'message':'Invalid email or password',
                            'data':serializer.errors
                            })
            
            elif user_data.is_varified == True:
                return Response({
                    "Error":"User is not Varified."
                })
            
            user=login(request, user)
            return Response({
                    'data':serializer.data,
                    'status':status.HTTP_200_OK,
                    'message':"You are logged in succssfully"
                    })
            
        return Response({
                        'status':status.HTTP_400_BAD_REQUEST,
                        'message':'Invalid email or password',
                        'data':serializer.errors
                         })


class Varify_User(viewsets.ViewSet):
    queryset = UserModel.objects.all()
    serializer_class = Varify_User_Serializer

    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
    
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            otp = serializer.validated_data.get('otp')

            s_email = request.session.get('email')
            s_otp = request.session.get('otp')

            if email == str(s_email) and otp == str(s_otp):
                user = UserModel.objects.filter(email=email).first()
                user.is_varified = True
                user.save()
                return Response({'message':'User Varified',
                                 'status':status.HTTP_200_OK
                                 })
        return Response({'message':'something went wrong!',
                          'status':status.HTTP_400_BAD_REQUEST
                        })
    

class Transaction_Records(viewsets.ModelViewSet):
    queryset = Block_Of_Transactions.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'user_id']
    http_method_names = ['get', 'post']

    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data = data)
        if serializer.is_valid(raise_exception = True):
            Transaction_obj = Block_Of_Transactions()
            Transaction_obj.user_id = serializer.validated_data.get('user_id')
            Transaction_obj.amount_paid = serializer.validated_data.get('amount_paid')
            if len(serializer.validated_data.get('from_account'))<16 and len(serializer.validated_data.get('from_account'))>16:
                return Response({"Error":"Invalid Card"})
            Transaction_obj.from_account = serializer.validated_data.get('from_account')
            if len(serializer.validated_data.get('Adhar_number'))<12 and len(serializer.validated_data.get('Adhar_number'))>12 :
                return Response({"Error":"Invalid Card"})
            Transaction_obj.Adhar_number = serializer.validated_data.get('Adhar_number')
            Transaction_obj.PAN_Number = serializer.validated_data.get('Pan_Number')
            Transaction_obj.message = serializer.validated_data.get('message')
            Transaction_obj.save()
            Transaction_obj.hash = Block_Of_Transactions().create_hash(Transaction_obj)
            Transaction_obj.prev_hash = Block_Of_Transactions().get_prev_hash(Transaction_obj)
            Transaction_obj.save()
            return Response(self.serializer_class(Transaction_obj).data)
        return Response({"message":"Something went wrong"})
from rest_framework import serializers
from .emails import send_email
from .models import UserModel, Block_Of_Transactions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'name', 'phone_number', 'phone_number', 'role', 'address', 'password']

    def create(self, validate_data):
        user = UserModel.objects.create(username = validate_data['username'],
                                        email = validate_data['email'],
                                        name = validate_data['name'],
                                        phone_number = validate_data['phone_number'],
                                        role = validate_data['role'],
                                        address = validate_data['address'],
                                        )
        user.set_password(validate_data['password'])
        user.save()
        return user

class Login_Serializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class Varify_User_Serializer(serializers.Serializer):
    email = serializers.CharField(max_length = 50)
    otp = serializers.CharField(max_length = 10)

class TransactionSerializer(serializers.ModelSerializer):
    donor = UserSerializer(read_only=True)
    class Meta:
        model = Block_Of_Transactions
        fields = '__all__'

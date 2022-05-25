from rest_framework import serializers
from .models import CustomUser, Driver, DriverManager, Head, Manager, Vehicle

Type_choices =( 
    ("Head", "Head"), 
    ("Driver", "Driver"), 
    ("Manager", "Manager")
)
 

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}
    ,write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email','username','first_name','last_name','Types','password','password2']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password!=password2:
            raise serializers.ValidationError('please confirm passowrd')
        return attrs
    
    def create(self,validate_data):
        return CustomUser.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
     
    class Meta:
        model = CustomUser
        fields = ['email','password']

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class DriverRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}
    ,write_only=True)
    # type = CustomUser.Types.Driver
    type = CustomUser.Types.choices
    class Meta:
        model = Driver
        fields = ['email','username','first_name','last_name','type','password','password2']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    
    def validate(self, attrs):
        # if CustomUser.objects.filter()
        password = attrs.get('password')
        password2 = attrs.get('password2')
        # type = attrs.get('type')
        if password!=password2:
            raise serializers.ValidationError('please confirm passowrd')
        return attrs
    
    def create(self,validate_data):
        Driver.objects.create(**validate_data)
        return Driver.Types.Driver

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class HeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Head
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'



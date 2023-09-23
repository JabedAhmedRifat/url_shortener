from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

#generate email for forget Password
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from django.contrib.auth.tokens import PasswordResetTokenGenerator

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password','username']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email= validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email']    

    
class LoginUserSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("wrong Credential")
    
#change Password
 
class ChangePasswordSerializer(serializers.Serializer):
        old_password = serializers.CharField()
        new_password = serializers.CharField()
        

# Reset Password

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
    def validate_email(self,email):
        try :
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("user with this email does not exist")
        
        uid  = urlsafe_base64_encode(force_bytes(user.pk))
        token = PasswordResetTokenGenerator().make_token(user)
        
        self.user = user
        self.uid = uid
        self.token = token
        
        return email
    
    
class SetNewPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField()
    
    def set_new_password(self, uid, token):
        uid = urlsafe_base64_decode(uid)
        token = str(token)
        try:
            user = User.objects.get(pk=uid)
            
            if PasswordResetTokenGenerator().check_token(user, token):
                new_password = self.validated_data['new_password']
                user.set_password(new_password)
                user.save()
                return user
        
        except User.DoesNotExist:
            pass 
        
        return None
            
            
            
            
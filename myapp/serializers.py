from rest_framework import serializers
from myapp.models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id','first_name','last_name','username','email','password')
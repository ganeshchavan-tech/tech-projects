from rest_framework.serializers import ModelSerializer
from .models import Accounts, Employees
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class AccountsSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Accounts
        fields = ['id', 'username', 'password', 'role']

    def create(self, validated_data):
        user = Accounts.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employees
        fields = ['employee', 'employee_name']
        depth = 1
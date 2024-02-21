from .models import Accounts
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class registerSerializar(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Accounts
        fields = "__all__"

    def create(self, validated_data):
        user = Accounts.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user
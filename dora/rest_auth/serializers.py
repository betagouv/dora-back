from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers

from dora.sirene.models import Establishment
from dora.users.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"),
                email=email,
                password=password,
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = "Unable to log in with provided credentials."
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class TokenSerializer(serializers.Serializer):
    key = serializers.CharField()


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField()


class ResendEmailValidationSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ServiceAndUserSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    siret = serializers.CharField()

    def validate_email(self, value):
        try:
            User.objects.get(email=value)
            raise serializers.ValidationError("Cet utilisateur existe déjà")
        except User.DoesNotExist:
            return value

    def validate(self, attrs):
        name = attrs.get("name")
        email = attrs.get("email")
        password = attrs.get("password")
        siret = attrs.get("siret")
        tmp_user = User(name=name, email=email)

        try:
            validate_password(password, tmp_user)
        except DjangoValidationError as exc:
            raise serializers.ValidationError({"password": list(exc.messages)})

        try:
            establishment = Establishment.objects.get(siret=siret)
            attrs["establishment"] = establishment
        except Establishment.DoesNotExist:
            # The SIRET field is hidden on the frontend, so display this error globally
            # TODO: Ideally it should be the frontend role to display the message anyway
            raise serializers.ValidationError({"non_field_errors": "SIRET inconnu"})

        return super().validate(attrs)
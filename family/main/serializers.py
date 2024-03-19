from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, Serializer, CharField, ValidationError
from .models import Family, Member, Assessment, Wish


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class FamilySerializer (ModelSerializer):
    members = MemberSerializer(many=True)

    class Meta:
        model = Family
        fields = ['name', 'id', 'members']


class AssessmentSerializer(ModelSerializer):
    member_target = MemberSerializer()
    member_source = MemberSerializer()

    class Meta:
        model = Assessment
        fields = '__all__'


class AssessmentCreateSerializer(ModelSerializer):
    class Meta:
        model = Assessment
        fields = ['value', 'comment', 'member_target', ]


class LoginSerializer(Serializer):
    username = CharField(
        label="Login",
        write_only="true"
    )

    password = CharField(
        label="Hasło",
        write_only="true",
        trim_whitespace=False,
        style={'input_type': 'password'}
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs


class UserSerializer (ModelSerializer):
    members = MemberSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'username', 'email', 'members']


class WishSerializer (ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Wish
        fields = '__all__'

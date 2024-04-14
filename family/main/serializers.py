from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.serializers import (
    ModelSerializer, Serializer, CharField, ValidationError,
    SerializerMethodField, ChoiceField, HiddenField, CurrentUserDefault)
from .models import Family, Member, Assessment, Wish


class UserReadSerializer (ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'username', 'email', 'members']


class MemberSerializer(ModelSerializer):
    user = UserReadSerializer(read_only=True)

    class Meta:
        model = Member
        fields = '__all__'
        depth = 2


class FamilySerializer (ModelSerializer):
    members = MemberSerializer(many=True, read_only=True)
    user_id = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Family
        fields = ['name', 'id', 'members', 'user_id']

    def create(self, validated_data):
        newFamily = Family.objects.create(
            **{k: v for (k, v) in validated_data.items() if k == 'name'}
        )

        memberUser = validated_data['user_id']

        newMemberData = dict(
            user=memberUser,
            name=memberUser.username,
            is_user=True,
            family=newFamily,
            is_boss=True
        )
        Member.objects.create(**newMemberData)
        return newFamily


class AssessmentSerializer(ModelSerializer):
    member_target = MemberSerializer()
    member_source = MemberSerializer()
    plus_count = SerializerMethodField(read_only=True)
    minus_count = SerializerMethodField(read_only=True)

    def get_plus_count(self, obj):
        return Assessment.objects.filter(
            member_target_id=obj.member_target_id,
            value=1
        ).count()

    def get_minus_count(self, obj):
        return Assessment.objects.filter(
            member_target_id=obj.member_target_id,
            value=-1
        ).count()

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


class WishReadSerializer (ModelSerializer):
    owner_user = UserSerializer()
    owner_member = MemberSerializer()
    status = ChoiceField(choices=Wish.Status.choices)
    status_value = SerializerMethodField()

    def get_status_value(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Wish
        fields = ['owner_user', 'owner_member', 'status', 'id', 'created_on',
                  'descriprion', 'status_value', 'provider']


class WishWriteSerializer (ModelSerializer):
    # owner_user = UserSerializer()
    # owner_member = MemberSerializer()

    class Meta:
        model = Wish
        fields = '__all__'

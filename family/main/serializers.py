from pandas import DataFrame
from rest_framework.serializers import ModelSerializer
from .models import Family, Member


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class FamilySerializer (ModelSerializer):
    members = MemberSerializer(many=True)

    class Meta:
        model = Family
        fields = ['name', 'id', 'members']

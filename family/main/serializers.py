from rest_framework.serializers import ModelSerializer
from .models import Family, Member, Assessment


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

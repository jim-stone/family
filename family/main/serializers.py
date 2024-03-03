from pandas import DataFrame
from rest_framework.serializers import ModelSerializer
from .models import Family


class FamilySerializer (ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'

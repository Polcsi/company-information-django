from rest_framework import serializers
from ..models.company_model import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['companyID', 'name', 'email', 'description']
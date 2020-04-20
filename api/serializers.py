from rest_framework import serializers
from pharmacy.models import Drug, Pharmacy, DrugPharmacy, Description


class DrugPharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugPharmacy
        fields = ['pharmacy', 'amount']


class DrugSerializer(serializers.ModelSerializer):
    pharmacies = DrugPharmacySerializer(source='drug_stocks', many=True)

    class Meta:
        model = Drug
        exclude = ['pharmacy']
        depth = 1


class DescriptionSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ['dosage_form', 'weight']


class DrugSearchSerializer(serializers.ModelSerializer):
    description = DescriptionSearchSerializer()

    class Meta:
        model = Drug
        fields = ['id', 'name', 'description', 'image']
        depth = 1


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'
        depth = 1


class PharmacySearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'
        depth = 1


class DrugPharmacySearchSerializer(serializers.ModelSerializer):
    pharmacy = PharmacySearchSerializer()

    class Meta:
        model = DrugPharmacy
        fields = ['pharmacy', 'amount', 'price']

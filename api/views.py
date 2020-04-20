from pharmacy.models import Drug, Pharmacy
from .serializers import DrugSerializer, PharmacySerializer, DrugSearchSerializer, DrugPharmacySearchSerializer,\
    DrugPharmacy
from rest_framework.response import Response
from rest_framework.views import APIView


class DrugView(APIView):
    @staticmethod
    def get(request, id):
        try:
            drug = Drug.objects.get(id=id)
        except Drug.DoesNotExist:
            return Response({'Error': 'NOT_FOUND'})

        serializer = DrugSerializer(drug)
        return Response(serializer.data)


class PharmacyView(APIView):
    @staticmethod
    def get(request, id):
        try:
            pharmacy = Pharmacy.objects.get(id=id)
        except Pharmacy.DoesNotExist:
            return Response({'Error': 'NOT_FOUND'})

        serializer = PharmacySerializer(pharmacy)
        return Response(serializer.data)


class DrugSearchView(APIView):
    @staticmethod
    def get(request, search):
        drugs = Drug.objects.filter(name__icontains=search)
        if drugs:
            serializer = DrugSearchSerializer(drugs, many=True)
            return Response(serializer.data)
        else:
            return Response({'Error': 'NOT_FOUND'})


class PharmacySearchView(APIView):
    @staticmethod
    def get(request, id):
        pharmacies = DrugPharmacy.objects.filter(drug=id)
        if pharmacies:
            serializer = DrugPharmacySearchSerializer(pharmacies, many=True)
            return Response(serializer.data)
        else:
            return Response({'Error': 'NOT_FOUND'})


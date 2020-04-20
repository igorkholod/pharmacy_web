from django.http import HttpResponseNotFound
from django.shortcuts import render
from pharmacy.models import Drug, Pharmacy
from django.views.decorators.http import require_http_methods


# Create your views here.
def main_page(request):
    return render(request, 'pharmacy/index.html')


@require_http_methods(['POST'])
def search_result(request):
    return render(request, 'pharmacy/search_result.html', {'search_term': request.POST['search_term']})


def pharmacy_result(request, id):
    return render(request, 'pharmacy/pharmacy_result.html', {'id': id})


def drug_info(request, id):
    try:
        Drug.objects.get(id=id)
    except Drug.DoesNotExist:
        return HttpResponseNotFound("Drug does not exist")
    return render(request, 'pharmacy/drug_info.html', {'id': id})


def about(request):
    return render(request, 'pharmacy/about.html')
from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(request, 'pharmacy/index.html')


def search_result(request):
    return render(request, 'pharmacy/search_result.html')


def pharmacy_result(request):
    return render(request, 'pharmacy/pharmacy_result.html')


def drug_info(request):
    return render(request, 'pharmacy/drug_info.html')


def about(request):
    return render(request, 'pharmacy/about.html')
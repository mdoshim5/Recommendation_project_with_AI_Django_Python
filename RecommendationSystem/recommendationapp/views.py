from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .aiengine import prediction, prediction2
from .packages import packages, packages_with_details
# Create your views here.

packages = packages
processor_names = ["Custom Intel Xeon E5-2076 v3 Haswell", "AWS Nitro System Xeon", "Intel Xeon Pentium 8176M"]
storage_type_names = ["EBS", "NVMe SSD", "HDD"]

def index(request):
    return render(request, "recommendationapp/recommendationapp.html")

def aboutUs(request):
    return render(request, "recommendationapp/aboutus.html")

def allpackages(request):
    return render(request, "recommendationapp/allpackages.html", {"database":packages_with_details})

def choseoptions(request):
    return render(request, "recommendationapp/choseoptions.html")

def dontknowmyrequirements(request):
    if request.method == "POST":
        company_size = request.POST["company_size"]
        hits = request.POST["hits"]
        package_number = prediction2(company_size, hits)
        package = packages_with_details[package_number]
        return render(request, "recommendationapp/dontknowreply.html", {"package_details": package})
    return render(request, "recommendationapp/dontknowmyrequirements.html")

def knowmyrequirements(request):
    if request.method == "POST":
        vcpu = request.POST["vcpu"]
        ram = request.POST["ram"]
        storage_type = request.POST["storage_type"]
        storage_amount = request.POST["storage_amount"]
        network_bandwidth = request.POST["network_bandwidth"]
        processor = request.POST["processor"]
        package_number = prediction(vcpu, ram, storage_type, storage_amount, network_bandwidth, processor)
        package = packages_with_details[package_number]
        return render(request, "recommendationapp/knowreply.html", {"package_details": package})
    return render(request, "recommendationapp/knowmyrequirements.html")
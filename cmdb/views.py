from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World.")

def cmdb(request):
    return HttpResponse("You're at the cmdb")

def asset(request, asset_id):
    return HttpResponse(f"You're at the asset {asset_id}")
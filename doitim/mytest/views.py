from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def json_response(request):
    return JsonResponse({"instance":"instance"}, status = 200)
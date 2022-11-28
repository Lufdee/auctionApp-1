from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from mainApp.models import User

""" index page view which returns the number of objects in the database """
def index(request: HttpRequest) -> HttpResponse:
    title = "User List"
    return render(request, "mainapp/index.html", {
        'title': title,
        'n': User.objects.all().count()
    })
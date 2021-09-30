from django.shortcuts import render
from django.http import request
import git

# Create your views here.
def webhook_update(request):
    file = open("victory.yes", "w+")
    if request.method == "POST":
        print("IT'S GIT UPDATE BABY")

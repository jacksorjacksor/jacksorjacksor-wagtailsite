from django.shortcuts import render
from django.http import request
import git

# Create your views here.
def webhook_update(request):
    print("Anything?")
    if request.method == "POST":
        print("IT'S GIT UPDATE BABY")

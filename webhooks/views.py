from django.shortcuts import render
from django.http import request
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import git

# Create your views here.
@require_POST
@csrf_exempt
def webhook_update(request):
    print("IT'S GIT UPDATE BABY")

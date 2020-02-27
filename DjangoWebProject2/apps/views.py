from django.shortcuts import render
from datetime import datetime
import time


# Create your views here.
def hello(request):
    now = datetime.now()
    context = {
        'current_date': now,
    }
    return render(request, "apps/index.html", context)
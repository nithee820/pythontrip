from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Location
from .models import Founders


# Create your views here.
def home(request):
    obj = Location.objects.all()
    pro = Founders.objects.all()

    return render(request, "index.html", {'res': obj, 'result1': pro})

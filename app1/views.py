from django.shortcuts import render

# Create your views here.

def one(request):
    data='this is from app1 data'
    d={'assumption':data}
    return render(request,'one.html',d)

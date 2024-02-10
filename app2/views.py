from django.shortcuts import render

# Create your views here.

def two(request):
    data_render='this is from app2 data'
    d={'assumption':data_render}
    return render(request,'two.html',d)

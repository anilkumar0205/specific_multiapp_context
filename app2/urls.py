from app2.views import *

from django.urls import path

app_name='multi'

urlpatterns=[
    path('two/',two,name='two')
]
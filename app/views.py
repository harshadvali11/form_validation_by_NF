from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def student(request):
    SFO=StudentForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('data is not Valid')
    return render(request,'student.html',d)








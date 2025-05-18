from django.shortcuts import render
from django.http import HttpResponse
from .utilites import pptparser

# Create your views here.
def home(request):
    return render(request, "askme/home.html")

def fileupload(request):
    if request.method == 'POST':
        myfile = request.FILES.get('file')
        pptparser.getText(myfile)

        return HttpResponse("Everything good and uploaded")
    return HttpResponse("something is wrong")
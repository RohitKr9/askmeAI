from django.shortcuts import render
from django.http import HttpResponse
from .utilites import pptparser, pdfparser, docxparser

# Create your views here.
def home(request):
    return render(request, "askme/home.html")

def fileupload(request):
    if request.method == 'POST':
        myfile = request.FILES.get('file')
        myfile_binary = myfile.read()

        if myfile.content_type == 'application/vnd.openxmlformats-officedocument.presentationml.presentation':
            pptparser.getText(myfile)
        
        elif myfile.content_type == 'application/pdf':
            pdfparser.getText(myfile_binary)

        elif myfile.content_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            docxparser.getText(myfile)

        return HttpResponse("Everything good and uploaded")
    return HttpResponse("something is wrong")
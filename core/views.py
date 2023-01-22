from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
# Create your views here.
def home(request):
    return render(request, 'index.html')

def categorey(request, catid):
    if(request):
       return HttpResponse(f"<p>{catid}</p>")
    
    else:
        return redirect('404')
    # return HttpResponse(f"<p>{catid}</p>")
def archive(request, year):
    if int(year) <= 2023:
        return HttpResponse(f"<h1>{year}</h1>")    
    else:
        return redirect('404')
def notfound(request):
    return render(request, '404.html')
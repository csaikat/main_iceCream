from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("this is Home")
    return render(request,"index.html")
def about(request):
    return HttpResponse("this is about")
def service(request):
    return HttpResponse("this is service")
def contact(request):
    return HttpResponse("this is contact")

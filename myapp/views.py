from django.shortcuts import render
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about us.html')
def contact(request):
    return render(request,'contact.html')
def gallery(request):
    return render(request,'gallery.html')
# Create your views here.

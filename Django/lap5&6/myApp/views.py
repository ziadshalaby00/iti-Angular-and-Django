from django.shortcuts import render
from django.http import HttpResponse

def home(request):
            return HttpResponse("""
        <div style="width:100vw; height:90vh; display:flex; justify-content: center; align-items:center;">
            <div>
                <h1 style="font-size: 62px; color: #ff5656; box-shadow:5px 5px 5px rgba(0,0,0,0.5);
                padding: 20px; border-radius: 20px; background-color: #6161df">
                    welcome
                </h1> 
                <div style="display:flex; justify-content: center; gap:20px">
                    <a href="contactUs/" style="padding: 10px; border-radius: 20px; border:none;
                    background-color:rgb(235, 73, 73); cursor: pointer;
                    color:white; box-shadow:5px 5px 5px rgba(0,0,0,0.5)">contact us</a>
                    <a href="aboutUs/" style="padding: 10px; border-radius: 20px; border:none;
                    background-color:rgb(54, 109, 228); cursor: pointer;
                    color:white; box-shadow:5px 5px 5px rgba(0,0,0,0.5)">about us</a>
                </div>
            </div>           
        </div>
        """)

def contactUs(request):
    return render(request, "contactUs.html")

def aboutUs(request):
    return render(request, "aboutUs.html")

def contactUsDataShow(request):
    return render(request, "contactUsDataShow.html")
# Create your views here.
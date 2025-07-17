from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Farmer,opinion
from django.contrib import messages
import joblib

# Create your views here.
def home(request):
    if request.method=="POST":
        tex=request.POST.get("te")
        if tex:
            obj1=opinion(op=tex)
            obj1.save()
        return redirect("home")
    all_opinions = opinion.objects.order_by('-created_at')  # most recent first
    return render(request, 'home.html', {'opinions': all_opinions})
def register(request):
    if request.method=="POST":
        n=request.POST.get("uname")
        e=request.POST.get("uemail")
        p=request.POST.get("unum")
        if Farmer.objects.filter(Email=e).exists():
            messages.error(request, "Email already registered. Please login.")
            return redirect("/login")
        obj=Farmer(Name=n,Email=e,Mnumber=p)
        obj.save()
        messages.success(request,"Registration Successful.Please login")
        return redirect("/login")
    return render(request,"register.html")
def login(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        uemail = request.POST.get("usermail")
        if not(Farmer.objects.filter(Name=uname, Email=uemail).exists()):
            messages.error(request, "Please enter registered email")
        else:
            return redirect("/crop2")  # or use a named URL with reverse()
    return render(request,"login.html")


model = joblib.load("crop_model.pkl")
le = joblib.load("label_encoder.pkl")
def crop(request):
    if request.method=="POST":
        N=request.POST.get("N")
        P=request.POST.get("P")
        K=request.POST.get("K")
        temperature=request.POST.get("T")
        humidity=request.POST.get("H")
        ph=request.POST.get("PH")
        rainfall=request.POST.get("R")
        print(N,P,K)
        xtest=[[N,P,K,temperature,humidity,ph,rainfall]]
        print(xtest)
        pred=model.predict(xtest)[0]
        crop = le.inverse_transform([pred])[0]
        print(crop)
        return render(request, "result.html", {"crop": crop})
    return render(request, "crop.html")

def result(request):
    return render(request,"result.html")
def delete(request):
    res=Farmer.objects.all()
    res.delete()
    res1=opinion.objects.all()
    res1.delete()
    
    
    return render(request,"delete.html")
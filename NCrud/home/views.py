from django.shortcuts import render
from .models import Student
def home(request):
    data=Student.objects.all()
    return render(request,"index.html")

def addstudent(request):
    s=Student()
    s.sname = request.POST["sname"]
    s.email = request.POST["email"]
    s.mobile = request.POST["mobile"]
    s.address = request.POST["address"]
    s.year = request.POST["year"]
    s.save()
    data=Student.objects.all()
    return render(request,"index.html",{"data":data})


def search(request):
    eid = request.POST["eid"]
    e = Student.objects.get(id=eid)
    return render(request,"index.html",{"data":[e]})


def delete(request):
    return render(request,"delete.html")


def delete_pro(request):
    eid = request.GET['eid']
    Student.objects.get(id=eid).delete()
    data = Student.objects.all()
    return render(request,"index.html",{"data":data})


def update(request):
    data = Student.objects.all()
    return render(request, "update.html",{"data":data})

def update_pro(request):
    s=Student()
    s.sname = request.POST["sname"]
    s.email = request.POST["email"]
    s.mobile = request.POST["mobile"]
    s.address = request.POST["address"]
    s.save()
    data = Student.objects.all()
    return render(request,"index.html",{"data":data})
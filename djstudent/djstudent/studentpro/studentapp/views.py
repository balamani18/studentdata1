from django.shortcuts import render
from .models import studata1
from. models import subjects 
def loadpage(request):
    return render(request,"home.html")

def start(request):
        if request.method=="POST" :
            return render(request,"add.html")
def upd(request):
       if request.method=="POST":
        return render(request,"update.html")
def delt(request):
       if request.method=="POST":
        return render(request,"delete.html")
def std(request):
    if request.method=="POST":
        return render(request,"addstu.html")
def upmark(request):
    if request.method=="POST":
        return render(request,"updatemarks.html")
def delmark(request):
    if request.method=="POST":
        return render(request,"delmark.html")

def stuinfo(request):
    if request.method=="POST":
        try:
            sname=request.POST['sn']
            sdept=request.POST['sd']
            sage=int(request.POST['sa'])
            snumber=int(request.POST['sm'])
            semail=request.POST['se']
            si=studata1(Name=sname,Dept=sdept,Age=sage,Mobile=snumber,Email=semail)
            si.save()
            res="STUDENT DATA SAVED...."
        except:
            res="STUDENT DATA NOT SAVED..."
        return render(request,"add.html",{'r':res})


def updateinfo(request):
   if request.method=="POST":
        try:
            sname=request.POST['sn']
            snumber=int(request.POST['sm'])
            si=studata1.objects.get(Name=sname)
            si.Mobile=snumber
            si.save()
            res="STUDENT DATA UPDATED...."
        except:
            res="STUDENT DATA NOT UPDATED..."
        return render(request,"update.html",{'r':res})
def deleteinfo(request):
    if request.method=="POST":
        try:
            sname=request.POST['sn']
            si=studata1.objects.get(Name=sname)
            si.delete()
            res="STUDENT DATA DELETED"
        except:
            res="STUDENT DATA NOT DELETED..."
        return render(request,"delete.html",{'r':res})
def stdmarks(request):
    if request.method=="POST":
        try:
            sdname=request.POST['sdn']
            sdmark1=int(request.POST['sm1'])
            sdmark2=int(request.POST['sm2'])
            sdmark3=int(request.POST['sm3'])
            sdmark4=int(request.POST['sm4'])
            sm=subjects(Student=sdname,Mark1=sdmark1,Mark2=sdmark2,Mark3=sdmark3,Mark4=sdmark4)
            sm.save()
            res="STUDENTS MARKS ADDED....."
        except:
            res="STUDENT MARKS NOT ADDED...."
        return render(request,"addstu.html",{'r':res})
def updtmark(request):
    if request.method=="POST":
        try:
            sdname=request.POST['sdn']
            sdmark1=int(request.POST['sm1'])
            sdmark2=int(request.POST['sm2'])
            sdmark3=int(request.POST['sm3'])
            sdmark4=int(request.POST['sm4'])
            sm=subjects.objects.get(Student=sdname)
            sm.Mark1=sdmark1
            sm.Mark2=sdmark2
            sm.Mark3=sdmark3
            sm.Mark4=sdmark4
            sm.save()
            res="STUDENT MARKS UPDATED"

        except:
            res="STUDENT MARKS NOT UPDATED..."
        return render(request,"updatemarks.html",{'r':res})
def deletemark(request):
       if request.method=="POST":
        try:
            sdname=request.POST['sdn']
            si=subjects.objects.get(Student=sdname)
            si.delete()
            res="STUDENT MARKS DELETED"
        except:
            res="STUDENT MARKS NOT DELETED..."
        return render(request,"delete.html",{'r':res})

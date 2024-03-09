from django.shortcuts import render,HttpResponse
from newapp.models import *


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        sn=request.POST.get('sn')
        br=request.POST.get('br')
        email=request.POST.get('email')
        sem=request.POST.get('sem')
        info=StudentInfo(studentName=sn,
                         studentBranch=br,
                         studentEmail=email,
                         studentSemester=sem)
        info.save()
        return render(request,'home.html')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        users=StudentInfo.objects.all()
        sn=request.POST.get('sn')
        email=request.POST.get('email')   
        for user in users:
            if user.studentName==sn:
                if user.studentEmail==email:
                    d={'user':user}
                    return render(request,'home.html',d)
                return HttpResponse('Invalid Password')
        else:
            return HttpResponse('invalid Username')
        
    return render(request,'login.html')


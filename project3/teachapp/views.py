from django.shortcuts import render
from teachapp.models import *

# Create your views here.
def homet(request):
    return render(request,'homet.html')

def teacher(request):
    if request.method=='POST':
        tn=request.POST.get('tn')
        sub=request.POST.get('sub')
        email=request.POST.get('email')
        info2=TeacherInfo(teacherName=tn,
                         teacherSubject=sub,
                         teacherEmail=email)
        info2.save()
        return render(request,'homet.html')

    return render(request,'teacher.html')

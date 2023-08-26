from django.shortcuts import render
from .models import user 
from .forms import studentregistration
from django.http import HttpResponseRedirect

# Create your views here.
def add_show(request):
    if request.method=="POST":
        fm=studentregistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            print(nm)
            reg=user(name=nm,email=em,password=pw)
            reg.save()
    else:
        fm=studentregistration()
    stud=user.objects.all()
    return render(request,'enroll/addandsave.html',{'form':fm,'stu':stud})
# function for delete record
def delete_data(request,id):
    if request.method=="POST":
        dl_id=user.objects.get(pk=id)
        dl_id.delete()
        return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method=="POST":
        ud_id=user.objects.get(pk=id)
        fm=studentregistration(request.POST,instance=ud_id)
        if fm.is_valid():
            fm.save()
    else:
        ud_id=user.objects.get(pk=id)
        fm=studentregistration(instance=ud_id)
    return render(request,'enroll/update.html',{'form':fm})
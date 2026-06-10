import datetime
from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from userapp.models import  student_attendence,student
# Create your views here.
def home(request):
    return render(request,'home.html') 

def loginpage(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user_login=authenticate(request,username=username,password=password)
        if user_login is not None:
            login(request,user_login)
            messages.success(request,"Login Success")
            return redirect('dashboard')
        else:
            messages.error(request,"Login Faild")
    return render(request,'login_page.html')

def signup(request):
    if request.method=='POST':
        first_name=request.POST["name"]
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        user_data=User.objects.create_user(first_name=first_name,username=username,email=email,password=password)
        user_data.save()
        messages.success(request,"Sign Up Success")
        return redirect('loginpage')
    else:
        print("Data Not Inserted")
        
    return render(request,'signup_page.html')
@login_required(login_url='dashboard.html')

def dashboard(request):
    st_data=student.objects.filter()
    st_leave=student_attendence.objects.filter(attendence=0)
    st_present = st_data.count() - st_leave.count()
    d={"st_data":st_data.count(),"st_leave":st_leave.count(), "st_present":st_present}
    return render(request,'dashboard.html',d)

def create_student(request):
    if request.method=='POST':
        name=request.POST['name']
        course=request.POST['course']
        age=request.POST['age']
        dob=request.POST['dob']
        doj=request.POST['doj']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        address=request.POST['address']
        st_at=student_attendence.objects.create(name=name,course=course)
        std_obj = student.objects.create(name=name,dob=dob,doj=doj,address=address,city=city,state=state,age=age,country=country,course=course)
        if st_at and std_obj is not None:
            st_at.save()
            std_obj.save()
            messages.success(request,"Student Added Sucessfully")
        else:
            messages.error(request,"Error Occuerd")
        return redirect('students_list')
    return render(request,'create_student.html')

def students_list(request):
    st_data=student.objects.all()
    d={'student':st_data}
    return render (request,'students_list.html',d)

def  delete_student(request,pid):
    del_data=student.objects.get(id=pid)
    if del_data is not None:
        del_data.delete()
        messages.success(request, "Deleted Success Fully")
        return redirect('students_list')
    else:
        messages.error(request, "Deleteion Faild")
        return redirect ('students_list')

def edit_student(request,pid):
    get_id=student.objects.get(id=pid)
    if request.method=='POST':
        name=request.POST['name']
        course=request.POST['course']
        age=request.POST['age']
        dob=request.POST['dob']
        doj=request.POST['doj']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        address=request.POST['address']
        edit_data=student.objects.filter(id=pid).update(name=name,dob=dob,doj=doj,address=address,city=city,state=state,age=age,country=country,course=course)
        if edit_data is not None:
            messages.success(request,"Update SuccessFully")
        else:
            messages.error(request,"Updation Faild")
    return render (request,'edit_student.html',{'get_id':get_id})

def attendence(request):
    st_data=student_attendence.objects.all()
    d={'student':st_data}
    return render(request,'attendence.html',d) 

def reg_attendence(request,pid):
    st_regat=student_attendence.objects.get(id=pid)
    date=datetime.date.today()
    if st_regat is not None:
        st_up=student_attendence.objects.filter(id=pid).update(date=date,attendence=1)
        if st_up is not None:
            messages.success(request,"Attendende Marked")
        else:
            messages.success(request,"Attendence Marked Faild")
    return redirect('attendence')

def reg_apsent(request,pid):
    st_regat=student_attendence.objects.get(id=pid)
    date=datetime.date.today()
    if st_regat is not None:
        st_up=student_attendence.objects.filter(id=pid).update(date=date,attendence=0)
        if st_up is not None:
            messages.success(request,"Attendende Marked")
        else:
            messages.success(request,"Attendence Marked Faild")
    return redirect('attendence')

def signout(request):
    logout(request)
    return redirect('loginpage')
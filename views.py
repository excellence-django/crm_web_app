from django.views.generic import View
from django.shortcuts import render,redirect
from django.contrib import messages
from studentapp.forms import Studentform,Courseform,Enrollform,EnrollSingleform
from studentapp.models import Student,Course,Enroll
from studentapp.forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.contrib.messages.storage import default_storage
from django import forms
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User

from django.core.mail import EmailMessage, get_connection
from django.conf import settings


def send_email(request):

    with get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_tls=settings.EMAIL_USE_TLS
    ) as connection:
        subject = "Django Test"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['', ]
        message = "from django"
        EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()

    return render(request, 'auth_home.html')
def sendEmail(request):
    email='egc.webdeveloper@gmail.com'
    user=User.objects.create_user(username='',
                                  password='',
                                  email=''
                                  )
    user = forms.Form().save(commit=False)

    user.save()
    login(request,user)
    subject="From django"
    message="Test mail"
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[user.email,]
    send_mail(subject,message,email_from,recipient_list)
    return redirect("index")
def sigin_required(func):
    print("Login")
    def wapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return func(request,*args,**kwargs)
        else:
            messages.error(request,"you must login")
            return redirect("index")
    return wapper

def logoutview(request, *args, **kwargs):
    logout(request)
    return redirect("index")

def Index(request):
    return render(request,"student_list.html")
def remove_student(request,*args,**kwargs):
    id=kwargs.get("sid")
    student=Student.objects.get(rollno=id)
    student.delete()
    system_messages = messages.get_messages(request)
    for message in system_messages:
        pass
    messages.success(request,"Student has been removed successfully")
    return redirect("list")

class StudentCreateView(View):
    def get(self,request,*args,**kwargs):
        form=Studentform()
        return render(request,"studentregister.html",{"forms":form})
    def post(self,request,*args,**kwargs):
        form=Studentform(request.POST,files=request.FILES)
        if form.is_valid():
            name=form.cleaned_data.get("name")

            form.save()
            system_messages = messages.get_messages(request)
            for message in system_messages:
                pass
            messages.success(request,"Student has been recorded successfully")
            return redirect("list")
        else:
            messages.error(request,"failed")
            return render(request,"studentregister.html",{"forms":form})


class StudentListView(View):
    def get(self,request):
        qs=Student.objects.all()
        return render(request,"student_list.html",{"students":qs})

@method_decorator(sigin_required,name="dispatch")
class StudentDetailView(View):
    def get(self,request,*args,**kwargs):
        sid=kwargs.get("stid")
        qs=Student.objects.get(rollno=sid)
        return render(request,"view.html",{"student":qs})

class StudentEditView(View):
    def get(self,request,*args,**kwargs):
        sid=kwargs.get("std_id")
        student=Student.objects.get(rollno=sid)
        form=Studentform(instance=student)
        return render(request,"edit.html",{"forms":form})

    def post(self,request,*args,**kwargs):
        sid=kwargs.get("std_id")
        student=Student.objects.get(rollno=sid)
        form=Studentform(request.POST,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,"Update success fully")
            return redirect("list")
        else:
            system_messages = messages.get_messages(request)
            for message in system_messages:
                pass
            messages.error(request,"error")
            return render(request,"edit.html",{"forms":form})


class LoginView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,"auth_login.html",{"forms":form})

    def  post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pword=form.cleaned_data.get("password")
            user = authenticate(username=uname, password=pword)
            if user:
                login(request,user)
                print("sucessfully")
                return redirect("home")
            else:
                system_messages = messages.get_messages(request)
                for message in system_messages:
                    pass
                messages.error(request,"invalid creation")
                print("error")
                return render(request,"auth_login.html",{"forms":form})

class CourseCreateView(View):
    def get(self,request,*args,**kwargs):
        form=Courseform()
        return render(request,"newcourse.html",{"forms":form})
    def post(self,request,*args,**kwargs):
        form=Courseform(request.POST,files=request.FILES)
        if form.is_valid():


            form.save()
            system_messages = messages.get_messages(request)
            for message in system_messages:
                pass
            messages.success(request,"Course has been recorded successfully")
            return redirect("clist")
        else:
            messages.error(request,"failed")
            return render(request,"newcourse.html",{"forms":form})

class CourseListView(View):
    def get(self,request):
        qs=Course.objects.all()
        return render(request,"course_list.html",{"courses":qs})

    def post(self,request,*args,**kwargs):
        sid=kwargs.get("std_id")
        student=Student.objects.get(rollno=sid)
        form=Studentform(request.POST,instance=student)
        system_messages = messages.get_messages(request)
        for message in system_messages:
            pass
        if form.is_valid():
            form.save()
            messages.success(request,"Update success fully")
            return redirect("list")
        else:
            messages.error(request,"error")
            return render(request,"edit.html",{"forms":form})

class CourseEditView(View):
    def get(self,request,*args,**kwargs):
        sid=kwargs.get("c_id")
        student=Course.objects.get(couse_id=sid)
        form=Courseform(instance=student)
        return render(request,"editcourse.html",{"forms":form})

    def post(self, request, *args, **kwargs):
        sid = kwargs.get("c_id")
        student = Course.objects.get(couse_id=sid)
        form = Courseform(request.POST, instance=student)
        system_messages = messages.get_messages(request)
        for message in system_messages:
            pass
        if form.is_valid():
            form.save()
            messages.success(request, "Update success fully")
            return redirect("clist")
        else:
            messages.error(request, "error")
            return render(request, "editcourse.html", {"forms": form})

def remove_course(request,*args,**kwargs):
    print("course")
    id=kwargs.get("cid")
    student=Course.objects.get(couse_id=id)
    student.delete()
    system_messages = messages.get_messages(request)
    for message in system_messages:
        pass
    messages.success(request,"Course has been removed successfully")
    return redirect("clist")



class CourseDetailView(View):
    def get(self,request,*args,**kwargs):
        sid=kwargs.get("cid")
        qs=Course.objects.get(couse_id=sid)
        return render(request,"cview.html",{"course":qs})


class EnrollCreateView(View):
    def get(self,request,*args,**kwargs):
        form = Enrollform()
        return render(request,"newenroll.html",{"forms":form})
    def post(self,request,*args,**kwargs):
        form=Enrollform(request.POST,files=request.FILES)
        if form.is_valid():


            form.save()
            system_messages = messages.get_messages(request)
            for message in system_messages:
                pass
            messages.success(request,"Enroll has been recorded successfully")
            return redirect("elist")
        else:
            messages.error(request,"failed")
            return render(request,"newenroll.html",{"forms":form})

class EnrollListView(View):
    def get(self,request):
        qs=Enroll.objects.all()
        return render(request,"enroll_list.html",{"enrolls": qs})

class EnrollEditView(View):
    def get(self,request,*args,**kwargs):
        sid=kwargs.get("e_id")
        enroll=Enroll.objects.get(e_id=sid)
        form=Enrollform(instance=enroll)
        return render(request,"editenroll.html",{"forms":form})

    def post(self, request, *args, **kwargs):
        sid = kwargs.get("e_id")
        enroll = Enroll.objects.get(e_id=sid)
        form = Enrollform(request.POST, instance=enroll)
        system_messages = messages.get_messages(request)
        for message in system_messages:
            pass
        if form.is_valid():
            form.save()
            messages.success(request, "Update success fully")
            return redirect("elist")
        else:
            messages.error(request, "error")
            return render(request, "editenroll.html", {"forms": form})
def remove_enroll(request,*args,**kwargs):
    id=kwargs.get("eid")
    print(id)
    enroll=Enroll.objects.get(e_id=id)
    enroll.delete()
    system_messages = messages.get_messages(request)
    for message in system_messages:
        pass
    messages.success(request,"Enroll has been removed successfully")
    return redirect("elist")

class EnrollDetailView(View):
    def get(self,request,*args,**kwargs):
        print("Hi")
        sid=kwargs.get("eid")
        qs=Enroll.objects.get(e_id=sid)
        return render(request,"eview.html",{"e":qs})

class HomeCreateView(View):
    def get(self,request,*args,**kwargs):

        return render(request,"homev.html")

class EnrollSingleView(View):
    def get(self,request,*args,**kwargs):
        form = EnrollSingleform()
        return render(request,"newenroll1.html",{"forms":form})

    def post(self, request, *args, **kwargs):
        form = EnrollSingleform(request.POST, files=request.FILES)
        if(form.is_valid()):
            e_id = form.cleaned_data.get("e_id")
            status = form.cleaned_data.get("status")
            Enroll.objects.filter(e_id=e_id.e_id).update(status=status)
            system_messages = messages.get_messages(request)
            for message in system_messages:
                pass
            messages.success(request, "Enroll status has been recorded successfully")
            return redirect("elist")

def en_info(request,*args,**kwargs):
    print("Teat")
    sid = kwargs.get("erid")
    print("Teat",sid)
    team = Enroll.objects.get(e_id=sid)
    print(team.rollno.rollno)
    student = Student.objects.get(rollno=team.rollno.rollno)
    course = Course.objects.get(couse_id=team.couse_id.couse_id)
    ser_instance = serializers.serialize('json', [team,])
    return JsonResponse({"eid": team.e_id,"details":team.details,"fees":team.fees,"Student":student.name,"Course":course.name,"status":team.status}, status=200)
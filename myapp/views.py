from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import studentform, TeacherForm, JobApplicationForm, loginform
from .models import student, teacher, JobApplication
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def hi(request):
    return render(request,'hi.html')
def page2(request):
    return render(request,'page2.html')

    
def display_form(request):
    if request.method == 'POST':
        form = studentform(request.POST, request.FILES)
        if form.is_valid():
            myname=form.cleaned_data['name']
            myage=form.cleaned_data['age']
            myemail=form.cleaned_data['email']
            mygender=form.cleaned_data['gender']
            myfile=form.cleaned_data['file']
            
            obj=student()
            obj.name=myname
            obj.age=myage
            obj.email=myemail
            obj.gender=mygender
            obj.file=myfile
            obj.save()
            
            # Re-render the form with a success message
            form = studentform()
            return render(request, 'studentform.html', {'form': form, 'success': True})  
        else:
            return render (request, 'studentform.html', {'form': form}) 
    else:
        form = studentform()
        return render(request, 'studentform.html', {'form': form})
    
    
def display_teacherform(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            myname=form.cleaned_data['name']
            mysubject=form.cleaned_data['subject']
            mygender=form.cleaned_data['gender']
            obj=teacher()
            obj.name=myname
            obj.subject=mysubject
            obj.gender=mygender
            obj.save()
            form = TeacherForm()
            return render(request, 'teacherform.html', {'form': form, 'success': True})  
        else:
            return render (request, 'teacherform.html', {'form': form}) 
    else:
        form = TeacherForm()
        return render(request, 'teacherform.html', {'form': form}) 
    
def management(request):
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            myname = form.cleaned_data['name']
            myage = form.cleaned_data['age']
            myemail = form.cleaned_data['email']
            mygender = form.cleaned_data['gender']
            obj = student()
            obj.name = myname
            obj.age = myage
            obj.email = myemail
            obj.gender = mygender
            obj.save()
            form = studentform()
            return render(request, 'management.html', {'form': form, 'success': True})
        else:
            return render(request, 'management.html', {'form': form})
    else:
        form = studentform()
        return render(request, 'management.html', {'form': form})     
    
    
def homepage(request):
    return render(request,'homepage.html') 


@login_required(login_url='login')
def about(request):
    mysession=request.session.get('mysession')
    
    if mysession:
     return render(request, 'about.html',{'mysession':mysession})
    else: 
      return redirect('login')


def viewalldata(request):
    data=student.objects.all()
    return render(request,'viewalldata.html',{'data':data})

def specificdata(request,userid):
    data=student.objects.get(id=userid)
    return render(request,'specificdata.html',{'s':data})

def courses(request):
    return render(request, 'courses.html') 



def contact(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_body = request.POST.get('message')
        from_email = settings.EMAIL_HOST_USER
        admin_email = settings.EMAIL_HOST_USER
        
        file=request.FILES['file']

        # Include user's email in the message
        # full_message = f"From: {user_email}\n\n{message_body}"
        object=EmailMessage(
            subject,
            message_body,
            from_email,
            [admin_email],
        )
        object.attach(file.name,file.read(),file.content_type)
        object.send()   
        

        # send_mail(
        #     subject,
        #     full_message,
        #     from_email,
        #     [admin_email],
        #     fail_silently=False,
        # )
        return HttpResponse("Email sent successfully")
    else:
        return render(request, 'email.html')

def resume_form(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = JobApplication.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                cover_letter=form.cleaned_data['cover_letter'],
                resume=request.FILES['resume']
            )
            application.save()

            # Send email to admin
            subject = 'New Job Application'
            message = f"""
            Name: {form.cleaned_data['name']}
            Email: {form.cleaned_data['email']}
            Phone: {form.cleaned_data['phone']}
            Cover Letter:
            {form.cleaned_data['cover_letter']}
            """
            admin_email = settings.EMAIL_HOST_USER
            email = EmailMessage(subject, message, to=[admin_email])
            resume_file = request.FILES['resume']
            email.attach(resume_file.name, resume_file.read(), resume_file.content_type)
            email.send()

            # Send confirmation email to user
            user_subject = 'Your application has been received'
            user_message = 'Thank you for applying. We have received your resume and will get back to you shortly.'
            user_email = form.cleaned_data['email']
            send_mail(user_subject, user_message, from_email=settings.EMAIL_HOST_USER, recipient_list=[user_email])

            return HttpResponse('Your application has been submitted successfully!')
    else:
        form = JobApplicationForm()
    return render(request, 'RESUME.html', {'form': form}) 

def login_view(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            myusername = form.cleaned_data['username']
            mypassword = form.cleaned_data['password']
            
            user = User.objects.filter(username=myusername).first()
            
            if user is not None and user.check_password(mypassword):
                login(request, user)
                request.session['mysession'] = myusername
                return redirect('about')
            else:
                form.add_error(None, "Invalid username or password")
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = loginform()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
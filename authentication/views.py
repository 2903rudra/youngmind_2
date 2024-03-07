from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .forms import *
from .models import*
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
            user = authenticate(request, email = email, password = password, role = role)
            if user is not None:
                login(request,user)
                if user.role == 'SPOC':
                    return redirect('spoc_dashboard_url')
                elif user.role == 'STUDENT':
                    return redirect('student_dashboard_url')
            else:
                return render(request,'login/login.html',{'form':form,'error':'Invalid login!!'})
        else:
            form = LoginForm()
        return render(request,'login/login.html',{'form':form})
    

def college_spoc_signup(request):
    if request.method == 'POST':
        form = CollegeSPOCSignupForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit = False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()

            return redirect('verification_email_sent_url')
    else:
        form = CollegeSPOCSignupForm()
    return render(request,'login/college_spoc_signup.html',{'form':form})

def college_student_signup(request):
    if request.method == 'POST':
        form = CollegeStudentSignupForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit = False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()

            return redirect('verification_email_sent_url')
    else:
        form = CollegeSPOCSignupForm()
    return render(request,'login/college_spoc_signup.html',{'form':form})


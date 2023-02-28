from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return render(request,'welcome.html')

def home(request):
    return render(request,'home.html')    

def login(request):
    return render(request,'login.html')

def otp(request):
    return render(request,'otp.html')

def resetpassword(request):
    return render(request,'resetpassword.html')

def sign(request):
    return render(request,'sign-up.html')

def feedback(request):
    return render(request,'feedback.html')

def share(request):
    return render(request,'share.html')

def about_us(request):
    return render(request,'about.html')

def terms(request):
    return render(request,'terms.html')

def policy(request):
    return render(request,'policy.html')


def profile_index(request):
    return render(request,'../templates/profile/profile_index.html')

def edit_profile(request):
    return render(request,'../templates/profile/edit_profile.html')

def profile_username(request):
    return render(request,'../templates/profile/profile_username.html')

def profile_password(request):
    return render(request,'../templates/profile/profile_password.html')


def appointment1(request):
    return render(request,'../templates/appointment/index.html')

def appointment2(request):
    return render(request,'../templates/appointment/new_appointment.html')


def developments1(request):
    return render(request,'../templates/developments/index.html')

def developments2(request):
    return render(request,'../templates/developments/details.html')


def complaint_box1(request):
    return render(request,'../templates/complaint_box/index.html')

def complaint_box2(request):
    return render(request,'../templates/complaint_box/details.html')

def complaint_box3(request):
    return render(request,'../templates/complaint_box/new.html')


def blood_bank1(request):
    return render(request,'../templates/blood_bank/add.html')

def blood_bank2(request):
    return render(request,'../templates/blood_bank/group.html')

def blood_bank3(request):
    return render(request,'../templates/blood_bank/index.html')

def blood_bank4(request):
    return render(request,'../templates/blood_bank/information.html')

def blood_bank5(request):
    return render(request,'../templates/blood_bank/list.html')

def blood_bank6(request):
    return render(request,'../templates/blood_bank/self.html')


def news(request):
    return render(request,'../templates/news/index.html')


def suggestions1(request):
    return render(request,'../templates/suggestions/details.html')

def suggestions2(request):
    return render(request,'../templates/suggestions/index.html')

def suggestions3(request):
    return render(request,'../templates/suggestions/new.html')


def contacts1(request):
    return render(request,'../templates/contacts/numbers.html')

def contacts2(request):
    return render(request,'../templates/contacts/index.html')

def contacts3(request):
    return render(request,'../templates/contacts/cm.html')


def social_media(request):
    return render(request,'../templates/social_media/profile_password.html')

# Create your views here.

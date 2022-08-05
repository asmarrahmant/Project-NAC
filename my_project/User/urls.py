from django.urls import path
from . import views

urlpatterns = [
    path('welcome',views.welcome, name='welcome'),
    path('home',views.home, name='home'),
    path('login',views.login, name='login'),
    path('sign-up',views.sign, name='sign'),
    path('feedback',views.feedback, name='feedback'),
    path('share',views.share, name='share'),
    path('about_us',views.about_us, name='about_us'),
    path('terms',views.terms, name='terms'),
    path('policy',views.policy, name='policy'),
    path('profile_index',views.profile_index, name='profile_index'),
    path('edit_profile',views.edit_profile, name='edit_profile'),
    path('profile_username',views.profile_username, name='profile_username'),
    path('profile_password',views.profile_password, name='profile_password'),


    path('appointment',views.appointment1, name='appointment'),
    path('new_appointment',views.appointment2, name='new_appointment'),
    path('developments_index',views.developments1, name='developments_index'),
    path('developments_details',views.developments2, name='developments_details'),

    path('complaint_box_index',views.complaint_box1, name='complaint_box_index'),
    path('complaint_box_details',views.complaint_box2, name='complaint_box_details'),
    path('complaint_box_new',views.complaint_box3, name='complaint_box_new'),

    path('blood_bank_add',views.blood_bank1, name='blood_bank_add'),
    path('blood_bank_group',views.blood_bank2, name='blood_bank_group'),
    path('blood_bank_index',views.blood_bank3, name='blood_bank_index'),
    path('blood_bank_information',views.blood_bank4, name='blood_bank_information'),
    path('blood_bank_list',views.blood_bank5, name='blood_bank_list'),
    path('blood_bank_self',views.blood_bank6, name='blood_bank_self'),

    path('news',views.news, name='news_index'),

    path('suggestions_details',views.suggestions1, name='suggestions_details'),
    path('suggestions_index',views.suggestions2, name='suggestions_index'),
    path('suggestions_new',views.suggestions3, name='suggestions_new'),

    path('contacts_numbers',views.contacts1, name='contacts_numbers'),
    path('contacts_index',views.contacts2, name='contacts_index'),
    path('contacts_cm',views.contacts3, name='contacts_cm'),

    path('social_media',views.social_media, name='social_media')
]
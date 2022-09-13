from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from random import randint
from django.core.mail import send_mail
from django.conf import settings
from django.conf.urls.static import static
from .models import *
import datetime

data = {
    'no_headers': ['register_page', 'login_page', 'forgot_pwd_page'],
}

# alert_system
def alert(type, text):
    data['alert'] = {
        'type': type,
        'text': text,
    }
    print('alert called.')

# load resume data
def view_resume(email):
    master = Master.objects.get(Email = email)
    user = User.objects.get(Master=master)
    print(user)
    data['resume_data'] = {
        'profile_data': user,
        'skills': Skill.objects.filter(User = user),
        'experiences' : Experience.objects.filter(User=user),
        'projects': Project.objects.filter(User=user), 
        'educations' : Education.objects.filter(User=user),
    }

def index(request):
    return render(request, 'index.html', data)

def register_page(request):
    data['current_page'] = 'register_page'
    return render(request, 'register_or_forgot_pwd_page.html', data)


def login_page(request):
    data['current_page'] = 'login_page'
    return render(request, 'login_page.html', data)

# load user data
def profile_data(request):
    print('session from profile data', request.session['email'])
    master = Master.objects.get(Email = request.session['email'])
    user = User.objects.get(Master = master)
    # print("user data: ", user.__dict__)
    new_user = {}
    
    for k,v in user.__dict__.items():
        if k.startswith('_'):
            continue
        new_user.setdefault(k, v)

    new_user['Username'] = '@' + user.Master.__dict__['Email'].split('@')[0]
    new_user['Image'] = settings.MEDIA_URL + new_user['Image']
    
    print("new user: ", new_user)
    data['profile_data'] = new_user
    data['board_universities'] = Board_University.objects.all()
    data['course_stream'] = Course_Stream.objects.all()
    
    data['my_educations'] = Education.objects.filter(User=user)
    data['my_experience'] = Experience.objects.filter(User=user)
    data['my_skill'] = Skill.objects.filter(User=user)
    data['my_project'] = Project.objects.filter(User=user)
    # gc = []
    # for i,j in gender_choice:
    #     gc.append({"value": i, "text": j})
    # # print(gc)
    # data['gender_choice'] = gc

def profile_page(request):
    if 'email' in request.session:
        profile_data(request)
        data['current_page'] = 'profile_page'
        return render(request, 'profile_page.html', data)
    return redirect(login_page)

def forgot_pwd_page(request):
    data['current_page'] = 'forgot_pwd_page'
    return render(request, 'register_or_forgot_pwd_page.html', data)

def resume_page(request):
    view_resume("pateldivu2930@gmail.com")
    data['current_page'] = 'resume_page'
    return render(request, 'resume_page.html', data)

# OTP Creation
def otp(request):
    otp_number = randint(1000, 9999)
    print("OTP is: ", otp_number)
    request.session['otp'] = otp_number

# send_otp
def send_otp(request, otp_for="reg"):
    otp(request)
    print('email', request.POST['email'])
    request.session['email'] = request.POST['email']

    email_to_list = [request.POST['email'],]

    subject = 'OTP for {otp_for} Registration'

    email_from = settings.EMAIL_HOST_USER

    message = f"Your One Time Password for verification is: {request.session['otp']}."

    send_mail(subject, message, email_from, email_to_list)

    alert('success', 'An OTP has sent to your email.')
    data.update({'next_step': 'otp'})
    
    return JsonResponse(data)

def mail_send(request):
    email_to_list = [request.POST['email'],]

    from_email = settings.EMAIL_HOST_USER

    subject = request.POST['subject']

    message = request.POST['message']
    url = f"/resume_page/@{request.POST['username']}"

    send_mail(subject, message, from_email, email_to_list)

    return redirect(url)

# verify otp
def varify_otp(request):
    # email = request.session['email']
    if request.session['otp'] == int(request.POST['otp']):
        # register(email, pwd)
        # master = Master.objects.get(Email=email)
        # master.Password = request.POST['new_password']
        print("verified.")
        alert('success', 'An OTP verified.')
        request.session['is_active'] = True
    else:
        print("Invalid OTP")
        # return redirect(forgot_pwd_page)
        alert('danger', 'Invalid OTP')
        return JsonResponse(data)
    
    # return redirect(login_page)
    data.update({'next_step': 'password'})
    return JsonResponse(data)

# registration functionality
def register(request):
    master = Master.objects.create(
        Email = request.session['email'],
        Password = request.POST['new_password'],
        IsActive = request.session['is_active'],
        
    )

    User.objects.create(Master = master)

    alert('success', 'Account created successfully.')
    
    data.update({'next_step': 'login_page'})
    return JsonResponse(data)

# forgot pwd functionality
def change_pwd(request):
    email = request.session['email']
    master = Master.objects.get(Email=email)
    print(request.POST)
    if 'current_password' in request.POST:
        if request.POST['current_password'] != master.Password:
            alert('warning', 'Please enter current password correctly.')
            data.update({'error': 'invalid current password.'})
    else:
        del request.session['email']
        data.update({'next_step': 'login_page'})
    
    master.Password = request.POST['new_password']
    master.save()
    alert('success', 'Password has changed successfully.')
    
    return JsonResponse(data)

import os
upload_path = os.path.join(settings.MEDIA_ROOT, 'users/profile/')
print('uplodad path: ', upload_path)
print('static url: ', settings.STATIC_ROOT)

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
print(STATIC_ROOT)

# remove profile photo
def remove_profile_image(request):
    master = Master.objects.get(Email = request.session['email'])
    user = User.objects.get(Master = master)
    
    # f = open(os.path.join(STATIC_ROOT, 'img/avatar.png'), 'rb')

    # print("bin data: ", user.Image.url.split('/')[-1])
    
    # n = open(os.path.join(upload_path, user.Image.url.split('/')[-1]), 'wb')
    
    # n.write(f.read())
    # n.close()
    # f.close()

    # print('image path: ', user.Image.url.split('/')[-1])
    os.remove(os.path.join(upload_path, user.Image.url.split('/')[-1]))
    
    user.Image = ""
    user.save()
    

    print('image removed.')
    data['image_uploaded'] = 'false'

    return redirect(profile_page)

# profile image upload
def profile_image_upload(request):
    master = Master.objects.get(Email = request.session['email'])
    user = User.objects.get(Master = master)

    if 'profile_image' in request.FILES:
        user.Image = request.FILES['profile_image']
        file_type = request.FILES['profile_image'].name.split('.')[-1]
        new_image_name = master.Email.split('@')[0] + "_profile_image"
        
        new_image_name = f"{new_image_name}.{file_type}"

        if new_image_name in os.listdir(upload_path):
            os.remove(os.path.join(upload_path, new_image_name))

        user.Image.name = new_image_name

        print("File type: ", new_image_name)
        user.save()
    
    return redirect(profile_page)

# profile update
def profile_update(request):
    master = Master.objects.get(Email = request.session['email'])
    user = User.objects.get(Master = master)

    date = request.POST['birth_date'].split('-')
    date = datetime.date(int(date[0]), int(date[1]), int(date[2]))

    print('date time ', date)
        
    user.FullName = request.POST['fullName']
    user.BirthDate = date
    user.Mobile = request.POST['mobile']
    user.About = request.POST['about']
    user.Country = request.POST['country']
    user.State = request.POST['state']
    user.City = request.POST['city']
    user.Address = request.POST['address']

    user.save()
    alert('success', 'Account updated successfully.')
    #return JsonResponse(data)
    return redirect(profile_page)

# add new edcation detail
def add_education(request):
    master = Master.objects.get(Email = request.session['email'])
    user = User.objects.get(Master = master)

    board_university = Board_University.objects.get(id=(request.POST['board_university']))
    course_stream = Course_Stream.objects.get(id=(request.POST['course_stream']))

    education = Education.objects.create(
        User = user,
        BoardUniversity = board_university,
        CourseStream = course_stream,

        StartDate = request.POST['start_date'],
        EndDate = request.POST['end_date'],
        Score = request.POST['score'],
        Description = request.POST['description'],
    )

    if request.POST['is_education_continue']:
        education.IsCompleted = True
    
    if request.POST['is_cgpa']:
        education.IsPercent = False

    education.save()

    return redirect(profile_page)

# edit education functionality
def edit_education(request, pk):
    education = Education.objects.get(id=pk)
    education.StartDate = education.StartDate.strftime("%Y-%m-%d")
    education.EndDate = education.EndDate.strftime("%Y-%m-%d")


    data['edit_education'] = education

    return redirect(profile_page)

# delete education functionality
def delete_education(request, pk):
    Education.objects.get(id=pk).delete()

    return redirect(profile_page)



# Login functionality
def login(request):
    email = request.POST['email']
    password = request.POST['password']
    error = object

    try:
        master = Master.objects.get(Email=email)
        if master.Password == password:
            # return redirect(profile_page)
            request.session['email'] = master.Email
            data.update({'url': 'profile_page'})
            alert('success', 'Account logged in successfully.')
            print(request.session['email'])
            return redirect(profile_page)
            # return JsonResponse(data)
        else:
            raise Exception("Incorrect password")

    except Master.DoesNotExist as err:
        print("User does not exist. Please check your email.")
        error = err.args[0]
    except Exception as err:
        error = err.args[0]
        print("Error: ", err)

    data.update({'error': error})
    
    print(data)
    # return JsonResponse(data)
    return redirect(login_page)

def add_skill(request):
    master = Master.objects.get(Email = request.session['email'])
    user = User.objects.get(Master = master)

    skill = Skill.objects.create(
        User = user,
        Skill = request.POST['skill'],
        Level = request.POST['level'],
    )

    skill.save()

    return redirect(profile_page)

def delete_skill(request, pk):
    Skill.objects.get(id=pk).delete()

    return redirect(profile_page)


def add_project(request):
    master = Master.objects.get(Email = request.session['email'])
    user = User.objects.get(Master = master)

    project = Project.objects.create(
        User = user,
        Title = request.POST['title'],
        Category = request.POST['category'],
        Description = request.POST['description'],
    )

    project.save()

    return redirect(profile_page)

def delete_project(request, pk):
    Project.objects.get(id=pk).delete()

    return redirect(profile_page)


def add_experience(request):
    master = Master.objects.get(Email = request.session['email'])
    user = User.objects.get(Master = master)

    experience = Experience.objects.create(
        User = user,
        JobTitle = request.POST['job_title'],
        Company = request.POST['company_name'],
        StartDate = request.POST['start_date'],
        EndDate = request.POST['end_date'],
        Description = request.POST['description'],
    )

    experience.save()

    return redirect(profile_page)


def delete_experience(request, pk):
    Experience.objects.get(id=pk).delete()

    return redirect(profile_page)


def add_reference(request):
    master = Master.objects.get(Email = request.session['email'])
    user = User.objects.get(Master = master)

    reference = Reference.objects.create(
        User = user,
        Link = request.POST['link'],
        Description = request.POST['description'],
    )

    reference.save()

    return redirect(profile_page)

# delete reference functionality
def delete_reference(request, pk):
    Reference.objects.get(id=pk).delete()

    return redirect(profile_page)

# logout
def logout(request):
    if 'email' in request.session:
        del request.session['email']

    return redirect(login_page)



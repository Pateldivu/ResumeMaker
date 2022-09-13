from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name="index"),
    #path('login_page/'),
    path('', login_page, name="login_page"),
    path('register_page/', register_page, name="register_page"),
    path('login/', login, name="login"),
    path('profile_page/', profile_page, name="profile_page"),
    path('forgot_pwd_page/', forgot_pwd_page, name="forgot_pwd_page"),
    path('send_otp/', send_otp, name="send_otp"),
    path('varify_otp/', varify_otp, name="varify_otp"),
    path('register/', register, name="register"),
    path('change_pwd/', change_pwd, name="change_pwd"),
    path('resume_page/', resume_page, name="resume_page"),
    path('profile_image_upload/', profile_image_upload, name="profile_image_upload"),
    path('profile_update/', profile_update, name="profile_update"),
    path('remove_profile_image/', remove_profile_image, name="remove_profile_image"),
    path('add_education/', add_education, name="add_education"),
    path('edit_education/<int:pk>/', edit_education, name="edit_education"),
    path('delete_education/<int:pk>/', delete_education, name="delete_education"),
    path('add_skill/', add_skill, name="add_skill"),
    path('delete_skill/<int:pk>/', delete_skill ,name="delete_skill"),
    path('add_experience/', add_experience ,name="add_experience"),
    path('delete_experience/<int:pk>/', delete_experience ,name="delete_experience"),
    path('add_project', add_project ,name="add_project"),
    path('delete_project/<int:pk>/', delete_project ,name="delete_project"),
    path('add_reference', add_reference, name="add_reference"),
    path('mail_send/', mail_send, name='mail_send'),
    path('resume_page/', resume_page, name="resume_page"),

    path('logout/', logout, name="logout"),
]
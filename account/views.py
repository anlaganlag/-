from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth  import authenticate,login
from .forms import LoginForm,RegistrationForm

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse('Wellcom You,已經驗證通過了')
            else:
                return HttpResponse('Sorry.用戶名或者密碼不對')
        else:
            return HttpResponse('非法登錄')


    if request.method == 'GET':
        login_form = LoginForm()
        return render(request,'account/login.html',{'form':login_form})


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valib():
            new_user = user_form.save(commit=False)

def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST) 
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponse("successfully")
            #return HttpResponseRedirect(reverse("account:user_login"))
        else:
            return HttpResponse("sorry, your can not register.")
    else:
        user_form = RegistrationForm()
        return render(request, "account/register.html", {"form": user_form})



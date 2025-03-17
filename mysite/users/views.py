import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fake_db import user_db
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as django_login


def user_list(request):
    """ 유저 리스트 페이지 """
    context = {"users": user_db}
    return render(request, "user_list.html", context)


def user_info(request, user_id):
    """ 특정 유저 상세 페이지 """
    user = next((user for user in user_db if user["id"] == user_id), None)
    if not user:
        return render(request, "user_not_found.html", status=404)

    context = {"user": user}
    return render(request, "user_info.html", context)

def sign_up(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)

    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        django_login(request, form.get_user())
        return redirect(settings.LOGIN_REDIRECT_URL)

    context = {'form': form}
    return render(request, 'registration/login.html', context)

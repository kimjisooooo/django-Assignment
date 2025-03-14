from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from fake_db import user_db

def home(request):
    """ 홈페이지 """
    return render(request, 'home.html')

def user_list(request):
    names = [{'id': key, 'name': value['이름']} for key, value in user_db.items()]
    return render(request, 'user_list.html', {'data': names})

def user_info(request, user_id):
    if user_id not in user_db:
        raise Http404('User not found')
    info = user_db[user_id]
    return render(request, 'user_info.html', {'data': info})

urlpatterns = [
    path('', home, name='home'),  # ✅ 루트 URL 추가
    path('users/', user_list, name='user_list'),
    path('users/<int:user_id>/', user_info, name='user_info'),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.http import Http404  # 추가
from todo.views import todo_list, todo_info
from users import views as user_views

def home(request):
    """ 홈페이지 """
    return render(request, 'home.html')

urlpatterns = [
    path('', home, name='home'),
    path('users/', user_views.user_list, name='user_list'),
    path('users/<int:user_id>/', user_views.user_info, name='user_info'),
    path('admin/', admin.site.urls),
    path('todo/', todo_list, name='todo_list'),
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', user_views.login_view, name='login'),
    path('accounts/signup/', user_views.sign_up, name='signup'),
]

from django.shortcuts import render
from mysite.fake_db import user_db


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

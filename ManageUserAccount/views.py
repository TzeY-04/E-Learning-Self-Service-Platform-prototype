from django.shortcuts import render, redirect, get_object_or_404
from app.models import Course, User, Student, Teacher
from django.contrib import messages
from app.views import ManageUserAccount

def manage_user_account(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        user = User.objects.filter(user_id=user_id).first()

        if "view" in request.POST:
            if user:
                return render(request, "ManageUserAccount/viewuser.html", {"user": user})
            else:
                messages.error(request, "User ID does not exist!")  
                return redirect("manageuseraccount")  

        elif "delete" in request.POST:
            if user:
                return render(request, "ManageUserAccount/deleteuser.html", {"user": user})
            else:
                messages.error(request, "User ID does not exist!")  
                return redirect("manageuseraccount")  

    return render(request, "ManageUserAccount/manageuseraccount.html")

def delete_user(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        user = User.objects.filter(user_id=user_id).first()

        if user:
            return render(request, "ManageUserAccount/deleteuser.html", {"user": user})
        else:
            messages.error(request, "User ID does not exist!")  
            return redirect("manageuseraccount")  

    return redirect("manageuseraccount")

def confirm_delete_user(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        user = User.objects.filter(user_id=user_id).first()

        if user:
            user.delete()
            messages.success(request, "Successfully deleted user account.")  
        else:
            messages.error(request, "User ID does not exist!")  

        return redirect("manageuseraccount")  

def view_user(request):
    user_id = request.GET.get("user_id")  
    user = User.objects.filter(user_id=user_id).first()

    if user:
        return render(request, "ManageUserAccount/viewuser.html", {"user": user})
    else:
        messages.error(request, "User ID does not exist!")  
        return redirect("manageuseraccount")  

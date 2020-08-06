from django.http import HttpResponse
from django.shortcuts import render,redirect


def allowed_users(allowed_roles=[]):
        def allow_user(view_func):
                def wrapper_func(request,*args,**kwargs):

                        group=None
                        if request.user.groups.exists():
                                group=request.user.groups.all()[0].name

                        if group in allowed_roles:
                                return view_func(request,*args,**kwargs)
                        else:
                                return HttpResponse("hello, "+str(request.user)+"!!!! Your are not allowed to access this.")
                return wrapper_func
        return allow_user


def admin_only(view_func):
        def wrapper_func(request,*args,**kwargs):
                group=None
                if request.user.groups.exists():
                        group=request.user.groups.all()[0].name
                if group=='admin':
                        return view_func(request,*args,**kwargs)
                elif group=='customer':
                        return redirect('/')
                else:
                        return HttpResponse("hello, "+str(request.user)+"!!!! Your are not allowed to access this.")
        return wrapper_func

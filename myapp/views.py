from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from myapp.forms import SignUpForm,LoginForm,PasswordResetForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout


class SignUpView(CreateView):
    model=User
    form_class=SignUpForm
    template_name="register.html"
    success_url=reverse_lazy("signin")
    def form_valid(self, form):
        messages.success(self.request,"account has been created")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)
class SignInView(FormView):
    model=User
    form_class=LoginForm
    template_name="login.html"
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            messages.error(request,"failed to login")
        return render(request,self.template_name,{"form":form})
class PasswordResetView(FormView):
    model=User
    template_name="password-reset.html"
    form_class=PasswordResetForm
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            email=form.cleaned_data.get("email")
            pwd1=form.cleaned_data.get("password1")
            pwd2=form.cleaned_data.get("password2")
            if pwd1==pwd2:
                try:
                    usr=User.objects.get(username=username,email=email)
                    
                    usr.set_password(pwd1)
                    usr.save()
                    messages.success(request,"password changed")
                    return redirect("signin")
                except Exception as e:
                    messages.error(request,"invalid ctredentials")
                    return render(request,self.template_name,{"form":form})
            else:
                messages.error(request,"password mismatch")
                return render(request,self.template_name,{"form":form})
class IndexView(TemplateView):
    template_name="index.html"
def signout(request,*args,**kwargs):
    logout(request)
    return redirect("signin")
    



    
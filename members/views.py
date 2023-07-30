from django.shortcuts import render
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import *
from .forms import *
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import *


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_member:
                return reverse('member_dashboard')
            elif user.is_management:
                return reverse('management_dashboard')
            elif user.is_vendor:
                return reverse('vendor_dashboard')
            
        else:
            return reverse('login')
        


class RegisterMemberView(CreateView):
    model = User
    form_class = MemberSignUpForm
    template_name = 'member/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'member'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')
  
    
class RegisterManagementView(CreateView):
    model = User
    form_class = ManagementSignUpForm
    template_name = 'management/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'management'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')
    

class RegisterVendorView(CreateView):
    model = User
    form_class = VendorSignUpForm
    template_name = 'vendor/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'vendor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


#@login_required
@member_required
def MemberDashboard(request):
    loans =  Loan.objects.filter(client=request.user.member)
    context = {
        'loans': loans
    }
    return render(request, 'member/dashboard.html', context)

@login_required
@management_required
def ManagementDashboard(request):
    loans =  Loan.objects.filter(client=request.user.management)
    context = {
        'loans': loans
    }
    return render(request, 'management/dashboard.html', context)


@login_required
@vendor_required
def VendorDashboard(request):
    loans =  Loan.objects.filter(client=request.user.vendor)
    context = {
        'loans': loans
    }
    return render(request, 'vendor/dashboard.html', context)




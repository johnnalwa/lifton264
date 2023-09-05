from django.shortcuts import render
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import *
from .forms import *
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm


def login(request):
    form = LoginForm
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


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
        #login(self.request, user)
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
        #login(self.request, user)
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
        #login(self.request, user)
        return redirect('login')


# @login_required
# @member_required
def MemberDashboard(request):
    #loans =  Loan.objects.filter(group_member_id=request.user.member)
    context = {
        'loans': 0
    }
    return render(request, 'member/dashboard.html', context)

# @login_required
# @management_required
def ManagementDashboard(request):
   # message_count = models.Messages.objects.filter(username='username', status=0).count()
    totalgroups = Group.objects.all().count()
    totalfarmers = Member.objects.all().count()
    totalloanproducts = LoanProduct.objects.all().count()
    totalproducts = Product.objects.all().count()
    activepenalties = Penalty.objects.all().count()
    totalvendors = Vendor.objects.all().count()
    #loans =  Loan.objects.filter(group_member_id=request.user.member)
    context = {
        'totalgroups': totalgroups,
        'totalfarmers': totalfarmers,
        'totalloanproducts': totalloanproducts,
        'totalproducts': totalproducts,
        'activepenalties': activepenalties,
        'totalvendors': totalvendors,
    }
    return render(request, 'management/dashboard.html', context)


# @login_required
# @vendor_required
def VendorDashboard(request):
    #loans =  Loan.objects.filter(group_member_id=request.user.member)
    context = {
        'loans': 0
    }
    return render(request, 'vendor/dashboard.html', context)

 
def CreateGroup(request):
    model = Group
    form_class = CreateGroupForm
    template_name = 'management/creategroup.html' 

    def form_valid(self, form):
        group = form.save()
        login(self.request, user)
        return redirect('creategroup')

def CreateGroup(request):
    #model = Group
    form = CreateGroupForm
    context = {
        'form':form
    } 
    return render(request, "management/create_group.html", context)

def password_change_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Update the session with the new user object
            return redirect('change_done')  # Redirect to a success page
    else:
        form = CustomPasswordChangeForm(request.user)
    
    return render(request, 'password_update.html', {'form': form})

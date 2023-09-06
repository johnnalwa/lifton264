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
    model = Group
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


def apply_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            # Process the loan application data and save it to the database
            # Redirect to a thank you page or another appropriate page
            return redirect('success')
    else:
        form = LoanForm()
    
    return render(request, 'loans.html', {'form': form})

def repay_loan(request):
    if request.method == 'POST':
        form = LoanRepaymentForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., update loan repayment status)
            

            return redirect('loan_repayment_success')  # Redirect to a success 
    else:
        form = LoanRepaymentForm()

    context = {'form': form}
    return render(request, 'repayment.html', context)

def penalty_form(request):
    if request.method == 'POST':
        form = PenaltyForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return redirect('penalty_form_success')  # Redirect to a success page
    else:
        form = PenaltyForm()

    return render(request, 'penalty_form.html', {'form': form})

def create_group_announcement(request):
    if request.method == 'POST':
        form = GroupAnnouncementForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            group_announcement = form.save()
            # Redirect to a success page or display a success message
            return redirect('success_page') 
    else:
        form = GroupAnnouncementForm()

    return render(request, 'group_announcement_form.html', {'form': form})

def create_loan_reminder(request):
    if request.method == 'POST':
        form = LoanReminderForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            loan_reminder = form.save()
            # Redirect to a success page or display a success message
            return redirect('success_page') 
    else:
        form = LoanReminderForm()

    return render(request, 'loan_reminder_form.html', {'form': form})

def vendor_form_view(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            # Process form data and save to the database
            form.save()
            # Redirect to a success page or do something else
    else:
        form = VendorForm()

    return render(request, 'vendor_form.html', {'form': form})

def product_form_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Process form data and save to the database
            form.save()
            # Redirect to a success page or do something else
    else:
        form = ProductForm()

    return render(request, 'product_form.html', {'form': form})

def trainings_page(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainings_page')  # Redirect to the same page after submission
    else:
        form = TrainingForm()

    trainings = Training.objects.all()

    context = {
        'form': form,
        'trainings': trainings,
    }

    return render(request, 'management/trainings_page.html', context)

def article_list(request, article_id=None):
    articles = Article.objects.all().order_by('-publish_date')
    selected_article = None

    if article_id:
        selected_article = get_object_or_404(Article, pk=article_id)

    return render(request, 'articles/article_list.html', {
        'articles': articles,
        'selected_article': selected_article,
        'article_form': ArticleForm(),  # Include an empty form
    })

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = request.user  # Set the author to the current user
            new_article.save()
            return redirect('article_list')

    # If the form is invalid or it's a GET request, render the form
    return render(request, 'management/article_list.html', {
        'articles': Article.objects.all().order_by('-publish_date'),
        'article_form': ArticleForm(),
    })
    
    
def list_groups(request):
    groups = Group.objects.all()  # Fetch all groups from the database
    return render(request, 'management/list_groups.html', {'groups': groups})

def weather_page(request):
    return render(request, 'management/weather_page.html')
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import *
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class MemberSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput())
    password2 = forms.CharField(label=("Confirm Password"), widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_member = True
        if commit:
            user.save()
        client = Member.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'))
        return user
    


class ManagementSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput())
    password2 = forms.CharField(label=("Confirm Password"), widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_management = True
        if commit:
            user.save()
        personell = ManagementAdmin.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'))
        return user
    



class CountySignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput())
    password2 = forms.CharField(label=("Confirm Password"), widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_county= True
        if commit:
            user.save()
        client = County.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'))
        return user
    
class VendorSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput())
    password2 = forms.CharField(label=("Confirm Password"), widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vendor= True
        if commit:
            user.save()
        client = Vendor.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'))
        return user
    



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    


class GroupForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea())
    

    class Meta:
        model = Group
        fields = ("__all__")


class GroupMembersForm(forms.ModelForm):
    #project = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = GroupMembers
        fields = ('member_id', 'group_id')

class SavingForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Saving
        fields = ("__all__" )


class VoucherForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Voucher
        fields = ("__all__" )

class LoanProductForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = LoanProduct
        fields = ("__all__" )




class LoanForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Loan
        fields = ("__all__" )


class LoanRepaymentForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = LoanRepayment
        fields = ("__all__" )


class PenaltyForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Penalty
        fields = ("__all__" )


class GroupAnnouncementForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = GroupAnnouncement
        fields = ("__all__" )

class LoanReminderForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = LoanReminder
        fields = ("__all__" )

class VendorForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Vendor
        fields = ("__all__" )


class ProductForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Vendor
        fields = ("__all__" )
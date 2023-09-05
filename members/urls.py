from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.login, name="login"),
    path('login/', views.LoginView.as_view(), name="user_login"),
    #path('login/',views.user_login, name="user_login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    
    path('member/dashboard/',views.MemberDashboard, name="member_dashboard"),
    path('member/register/',views.RegisterMemberView.as_view(), name="register_member"),
    
    path('management/dashboard/',views.ManagementDashboard, name="management_dashboard"),
    path('management/register/',views.RegisterManagementView.as_view(), name="register_management"),
    path('management/creategroup/',views.CreateGroup, name="creategroup"),
       
    path('vendor/dashboard/',views.VendorDashboard, name="vendor_dashboard"),
    path('vendor/register/',views.RegisterVendorView.as_view(), name="register_vendor"),
    
    path('password_change/', views.password_change_view, name='password_change'),
    # path('password_change/done/', views.change_done, name='change_done'),
]






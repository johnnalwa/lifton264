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
    
    path('applyloan/', views.apply_loan, name='applyloan'),
    path('management/loan-list/', views.loan_list, name='loan_list'),
    path('repayloan/', views.repay_loan, name='repayloan'),
    path('penalty-form/', views.penalty_form, name='penalty_form'),
    path('create_group_announcement/', views.create_group_announcement, name='create_group_announcement'),
    path('create_loan_reminder/', views.create_loan_reminder, name='create_loan_reminder'),
    path('vendor/add/', views.vendor_form_view, name='vendor_form'),
    path('management/add_product/', views.add_product, name='add_product'),
    path('list_vendors/', views.list_vendors, name='list_vendors'),
    path('products/', views.product_list, name='product_list'),


    
    path('management/dashboard/',views.ManagementDashboard, name="management_dashboard"),
    path('management/register/',views.RegisterManagementView.as_view(), name="register_management"),
    path('management/creategroup/',views.CreateGroup, name="creategroup"),
    path('management/list-groups/', views.list_groups, name='list_groups'),
       
    path('vendor/dashboard/',views.VendorDashboard, name="vendor_dashboard"),
    path('vendor/register/',views.RegisterVendorView.as_view(), name="register_vendor"),
    
    path('password_change/', views.password_change_view, name='password_change'),
    # path('password_change/done/', views.change_done, name='change_done'),
    
    path('management/trainings/', views.trainings_page, name='trainings_page'),
    path('management/upload_article/', views.upload_article, name='upload_article'),
    path('management/weather/', views.weather_page, name='weather_page'),
    
    path('management/counties/', views. county_list, name='county_list'),
    path('subcounties/', views.subcounty_list, name='subcounty_list'),
    path('wards/', views.ward_list, name='ward_list'),
    
    path('display_group_members/', views.display_group_members, name='display_group_members'),
    path('monthly_loan_data/', views.monthly_loan_data, name='monthly_loan_data'),


    path('member/profile/<str:username>/', views.profile, name='profile'),
    path('categories/', views.category_list, name='category_list'),         

    


]






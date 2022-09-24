from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('',views.dashboard,name='dashboard'),
        
    path('activate/<uidb64>/<token>',views.activate,name='activate'),
    path('ForgotPassword/',views.ForgotPassword,name='ForgotPassword'),
    path('ResetPassword_Validate/<uidb64>/<token>',views.ResetPassword_Validate,name='ResetPassword_Validate'),
    path('ResetPassword',views.ResetPassword,name='ResetPassword'),

]
from calendar import c
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    # path('dashboard/',views.dashboard,name='dashboard'),
    path('user_dashboard/',views.user_dashboard,name='user_dashboard'),
        
    path('activate/<uidb64>/<token>',views.activate,name='activate'),
    path('ForgotPassword/',views.ForgotPassword,name='ForgotPassword'),
    path('ResetPassword_Validate/<uidb64>/<token>',views.ResetPassword_Validate,name='ResetPassword_Validate'),
    path('ResetPassword',views.ResetPassword,name='ResetPassword'),
    
    path('my_orders/',views.my_orders,name='my_orders'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('change_password/',views.change_password,name='change_password'),
    path('order_details/<int:order_id>/',views.order_details,name='order_details'),
    # path('address_book/',views.address_book,name='address_book'),
    # path('add_address/',views.add_address,name='add_address'),
    path('cancel_order_user/<int:order_number>/', views.cancel_order_user, name='cancel_order_user'),
    # path('activate-address/',views.activate_address,name='activate-address'),
    

]
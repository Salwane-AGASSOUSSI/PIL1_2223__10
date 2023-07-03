from django.urls import path
from authentification.views import login_page,logout_page,signup_page,add_superuser,delete_superuser,superuser_list,account_requests,approve_account_request,succes,refus
from django.contrib.auth import views
urlpatterns = [
    path('', login_page, name='login'),
    path('deconnexion/',logout_page,name='logout'),
    path('inscription/', signup_page,name='signup'),
    path('add_sup/', add_superuser,name='add' ),
    path('del_sup/<int:pk>/', delete_superuser, name='del'),
    path('gestions/',superuser_list,name='gestions'),
    path('reset_password/',views.PasswordResetView.as_view(template_name='authentification/password_reset.html'), name='reset_password'),
    path('reset_password_send/', views.PasswordResetDoneView.as_view(template_name='authentification/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='authentification/password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/',views.PasswordResetCompleteView.as_view(template_name='authentification/password_reset_done.html'),name='password_reset_complete'),
    path('account_requests/',account_requests,name='account_requests'),
    path('approve_account_request/<int:pk>/',approve_account_request,name='approve'),
    path('refus/<int:pk>/',refus, name='refus'),
    path('success/',succes,name='success'),

]
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from users import views


urlpatterns = [    
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('reset-password/<str:code>/', views.reset_password, name='reset-password'),
    path('edit-account/', views.edit_account, name='account'),
    # path('choose-profile/<pk>', views.choose_profile, name='choose-profile'),
    # path('account-setup-wizard/', views.account_setup_wizard, name='account-setup'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from triibe_project.settings import FORM_ERROR_MESSAGE

from core.models import Entrepreneur
from users.models import User, PasswordRecovery
from users.forms import UserCreateForm, LoginForm


import uuid
from datetime import datetime

from utils.utility import Hasher
hasher = Hasher()

# @login_required
# def choose_profile(request, pk):
#     try:
#         entrepreneur = get_object_or_404(Entrepreneur, user_id=pk)
#         return redirect('users:feeds', pk=entrepreneur.id)
#     except:
#         return redirect('users:account-setup', pk=request.user.id)


# @login_required
# def account_setup_wizard(request):
#     # user = get_object_or_404(User, id=pk)
#     return render(request, 'users/account_setup.html', {})



# ------------------------------------------------------- #
# USER ID | EMAIL | OLD PASSWD | NEW PASSWD | TIMESTAMP | UUID



def logout_user(request):
    logout(request)
    return redirect('core:index')


def forgot_password(request):
    '''
        INPUT: the users email through a get request
        OUTPUT: create a unique hashed secret and set expiry date to today for recovery
    '''

    try:
        user = get_object_or_404(User, email=request.GET.get('email'))
        secret_key = str(uuid.uuid4())[:8]
        PasswordRecovery.objects.create(secret=secret_key, user=user,)
        secret_key_hashed = hasher.make_hash(secret_key)
        secret_as_str = secret_key_hashed.decode()
        print('xxx: ', secret_as_str)
        # email_body = render_to_string('email/recovery.html', kwargs={'user': user, 'code': secret_key_hashed}) #if this was you click the link else ignore
        # notify_user = send_mail(to=user.email, subject='Password Recovery', body=email_body)
        return redirect('users:reset-password')
    except:
        messages.warning(request, "User with this email doesn't exist on our system!")
    return render(request, 'users/forgot-password.html', {})



def reset_password(request, code):
    '''
        INPUT: takes an unexpired secret key and 
        OUTPUT: set a new password for the user of that key
    '''
    try:
        secret_as_bytes = str.encode(code)
        secret_key = hasher.reveal_hash(secret_as_bytes) #result is secret
        secret = get_object_or_404(PasswordRecovery, secret=secret_key)
        if secret.expires.strftime("%Y-%m-%d") != datetime.now().strftime("%Y-%m-%d"):
            return HttpResponseRedirect('/forgot-password/', 'Redirecting...')
        else:
            if request.method == "POST":
                reset_password_form = ResetPassForm(request.POST)
                if reset_password_form.is_valid():
                    user = get_object_or_404(User, email=secret_key.user.email)
                    new_pass = user.set_password(reset_password_form.cleaned_data['new_password']) #check that password 1 == 2 in form
                    new_pass.save()
                    messages.warning(request, "You've successfully changed your password. Login to continue")
                    return redirect('users:login')
                else:
                    messages.warning(request, "Invalid data entered!")
            else:
                reset_password_form = ResetPassForm()
                return render(request, 'users/reset-password.html', {'reset_pass_form': reset_password_form})
    except:
        messages.warning(request, "User with this email doesn't exist on our system!")
        return redirect('users:forgot-password')


def signup(request):
    if request.method == 'POST':    
        user_form = UserCreateForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            Entrepreneur.objects.create(user=user)
            return redirect('users:login')
    else:
        user_form = UserCreateForm()
        data = {'user_form': user_form}
        return render(request, 'users/signup.html', data)


def login_user(request):
    if request.method == 'POST':        
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']            
            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('core:dashboard')
            else:
                messages.warning(request, 'Invalid Login')
                return redirect('core:index')        
    else:
        login_form = LoginForm()
        data = {'login_form': login_form}
        return render(request, 'users/login.html', data)


def edit_account(request):
    entrp = get_object_or_404(Entrepreneur, user_id=request.user.id)
    # account_update_form = AccountUpdateForm()
    return render(request, 'users/edit-account.html', {'entrepreneur': entrp})



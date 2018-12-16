from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
# from actions.utils import create_action
# from actions.models import Action
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
# from common.decorators import ajax_required
# from .models import Contact
from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
# from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
# from .models import Profile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            create_action(new_user, 'has created an account')
            return render(request, 'account/register/register_done.html', {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register/register.html', {'user_form': user_form})

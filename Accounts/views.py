from django.shortcuts import get_object_or_404, render
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_list_or_404
from django.urls import reverse, reverse_lazy


from Accounts.forms import *
from Job.permission import is_user


def get_success_urls(request):
    """
    Handle Success Url After Login
    """
    if 'next' in request.GET and request.GET['next'] != '':
        return request.GET['netx']
    else:
        return reverse('Job:home')


def user_registration(request):
    """
    Handle user registration
    """
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect('Accounts:login')
    context = {
        'form': form,
    }
    return render(request, 'accounts/user-registration.html', context)


def company_registration(request):
    """
    Handle user registration
    """
    form = CompanyRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect('Accounts:login')
    context = {
        'form': form
    }
    return render(request, 'accounts/company-registration.html', context)


@login_required(login_url=reverse_lazy('Accounts:login'))
@is_user
def user_edit_profile(request, id=id):
    user = get_object_or_404(User, id=id)
    form = UserProfileEditForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your Profile was SuccessFully Updated!')
        return redirect(reverse("Accounts:edit-profile", kwargs={
            'id': form.id
        }))
    context = {
        'form': form,
    }
    return render(request, 'accounts/user-edit-profile.html', context)


def user_logIn(request):
    """
    Provides users to logIn
    """
    form = UserLoginForm(request.POST or None)

    if request.user.is_authenticated:
        return redirect('/')

    else:
        if request.method == 'POST':
            if form.is_valid():
                auth.login(request, form.get_user())
                return HttpResponseRedirect(get_success_urls(request))
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def user_logOut(request):
    """
    Provide the ability to logout
    """
    auth.logout(request)
    messages.success(request, 'You are Successfully logged out')
    return redirect('Accounts:login')

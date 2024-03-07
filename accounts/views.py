from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('portal:home')

    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/register.html', context)

@login_required
def profile(request):
    user = request.user
    

    context = {

    }

    return render(request, 'accounts/profile.html', context)


@login_required
def profile_edit(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # messages.success(request, "Changes Saved Successfully")
            return redirect('portal:home')
        # messages.warning(request, "Something happened")
    else:
        form = UserUpdateForm(instance=user)

    context = {
        'form': form,
    }

    return render(request, 'accounts/profile_edit.html', context)


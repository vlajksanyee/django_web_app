from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # Saves the new user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}\nYou can now log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    user_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)

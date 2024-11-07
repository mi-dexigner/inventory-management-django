from django.shortcuts import render,redirect
from .forms import CreateUserForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        context = {
            "form":form
        }
        return render(request,'user/register.html',context)



@login_required
def profile(request):
    return render(request,'user/profile.html')\

@login_required
def profile_update(request):
    if request.method =='POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)
    context = {
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request,'user/profile_update.html',context)
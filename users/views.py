from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import UserRegister,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request) :
  if request.method =='POST' :
    form = UserRegister(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Account created for {username}!')
      return redirect('blog-home')
  else:
    form = UserRegister()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
  if request.method == 'POST':
    uform = UserUpdateForm(request.POST,instance=request.user)
    pform = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
    if uform.is_valid() and pform.is_valid():
      uform.save()
      pform.save()
      messages.success(request, f'Your Account has been updated!')
      return redirect('profile')

  else :
    uform = UserUpdateForm(instance=request.user)
    pform = ProfileUpdateForm(instance=request.user.profile)

  data = {
      'uform':uform,
      'pform':pform
    }
  return render(request,'users/profile.html',data)



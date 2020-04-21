from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import UserRegister
from pprint import pprint
#import pdb; pdb.set_trace()

# Create your views here.
def register(request) :
  print('request')
  quit
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


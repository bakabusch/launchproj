from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request): #log user out
    logout(request)
    return HttpResponseRedirect(reverse('baseball:index'))

def register(request): #register
    if request.method != 'POST': #create blank registration form
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST) #process completed form

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('baseball:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)

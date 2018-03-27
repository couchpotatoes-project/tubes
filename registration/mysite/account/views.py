from django.shortcuts import render,redirect
from account.forms import RegistrationForm



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register/home')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'registration.html', args)
            
    
    
    
def success(request):
    return render(request, 'submit.html')
from django.shortcuts import render,redirect,render_to_response
from django.template  import RequestContext
from game.forms import RegistrationForm
from django.views.generic import TemplateView
import itertools

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "index.html" , context=None)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'registration.html', args)
    	
def home(request):
    if request.user.is_authenticated:
        request.session['username'] = request.user.username
        # session expires after 1800s
        request.session.set_expiry(1800)
        return render(request, 'game/tubes.html' ,  {'counter': itertools.count()})
    else:
        return redirect('/login')
	
def gamerule(request):
    return render(request, 'gamerule/gamerule.html' , context=None)

def tubes(request):
	iterator=itertools.count(start=1,step=1)
	return render(request, 'game/tubes.html' , {'counter': itertools.count()})
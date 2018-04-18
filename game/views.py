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
    return render(request, 'game/tubes.html' ,  {'counter': itertools.count()})
	
def gamerule(request):
    return render(request, 'gamerule/gamerule.html' , context=None)

def tubes(request):
	iterator=itertools.count(start=1,step=1)
	return render(request, 'game/tubes.html' , {'counter': itertools.count()})
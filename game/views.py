from django.shortcuts import render,redirect
from django.template  import RequestContext
from game.forms import RegistrationForm
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "index.html" , context=None)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
            #return render(request,'/home',context_instance=RequestContext(request))
        else:
            form = RegistrationForm()
            args = {'form': form}
            return render(request, 'registration.html', args)
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'registration.html', args)
    
def success(request):
    return render(request, 'submit.html')

def gamerule(request):
    return render(request, 'gamerule/gamerule.html' , context=None)
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "index.html" , context=None)


# class RulePageView(TemplateView):
#     def get(self, request, **kwargs):
#         return render(request, "gamerule.html" , context=None)

def gamerule(request):
    return render(request, 'comingsoon/gamerule.html' , context=None)


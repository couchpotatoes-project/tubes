from django.shortcuts import render,redirect,render_to_response
from django.template  import RequestContext
from game.forms import RegistrationForm
from game.models import Level, UserScore
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "index.html" , context=None)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'registration.html', args)
    	
def home(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			level = request.POST.get('level','').strip()
			objectList = []
			for object in Level.objects.filter(squares=level):
				objectList.append(object)
				
			levelId = {}
			for object in objectList:
				levelId[object.id] = object.levelId
			
			return render(request, 'game/levels.html' ,  {'squares': level , 'identity':levelId })
		else:
			request.session['username'] = request.user.username
			# session expires after 1800s
			request.session.set_expiry(1800)
			id = Level.objects.all()
			squares = []
			
			totals = {}
			completed = {}
			for q in id:
				totalLevels = 0
				completedLevels = 0
				if not q.squares in squares:
					squares.append(q.squares)
					for object in Level.objects.filter(squares=q.squares):
						totalLevels = totalLevels + 1
						try:
							levelscore = UserScore.objects.get(username=request.user.username,levelId=object.id)
							completedLevels = completedLevels + 1							
						except:
							completedLevels = completedLevels
					totals[q.squares] = totalLevels
					completed[q.squares] = completedLevels
			
			return render(request, 'game/home.html' ,  {'squares': squares, 'totalLevels':totals, 'completedLevels':completed})
	else:
		return redirect('login/')
	
def gamerule(request):
    return render(request, 'gamerule/gamerule.html' , context=None)

def tubes(request):
	if request.method == 'POST':
			level = request.POST.get('level','').strip()
			object = Level.objects.get(id=level)				
			squares = object.squares
			points = object.positions
			counter = []
			for i in range(0,squares*squares):
				counter.append(i+1)
			circleWidth = ((400/squares) - 5)
			rectangleWidth = (400/squares)
			return render(request, 'game/tubes.html' ,  {'squares': squares , 'identity':level , 'points':points, 'counter':counter, 'circleWidth':circleWidth, 'rectangleWidth':rectangleWidth})
	else:
		return redirect('login/')

def savescore(request):
	if request.method == 'POST':
		username = request.POST.get('username','').strip()
		level = request.POST.get('level','').strip()
		moves = request.POST.get('moves','').strip()
		time = request.POST.get('time','').strip()
		try:
			levelscore = UserScore.objects.get(username=username,levelId=level)
			if(int(moves) < levelscore.moves):
				userscore = UserScore.objects.get(username=username,levelId=level).update(moves=moves,time=time)
				userscore.save()
		except UserScore.DoesNotExist:
			userscore = UserScore(username=username,levelId=level,moves=moves,time=time)
			userscore.save()
		
		return redirect('home')
	else:
		return redirect('home')
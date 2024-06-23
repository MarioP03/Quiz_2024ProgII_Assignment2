import json
from django.http import JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.utils import timezone
from .models import PublicQuestions, Users, Leaderboard
from .forms import AddQuestionsForm, UserCreateForm, UserLoginForm, PointsForm
from django.conf import settings

class QuestionsView(View):
    def get(self, request):
        pass

@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def post(self, request, *args, **kwargs):
        if 'getoneuser' in request.path:
            return self.getone_user(request)
        elif 'register' in request.path:
            return self.register(request)
        elif 'login' in request.path:
            return self.login(request)
        elif 'logout' in request.path:
            return self.logout(request)
        return JsonResponse({'status':'error', 'message':'Invalid request method.'}, status = 400)
    
    def getone_user(self, request):
        data = json.loads(request.body)
        user = Users.objects.get(username = data['username'])
        if user is None:
            return JsonResponse({'status':'error', 'message':'User with does not exist.'}, status = 400)
        userdata = {
            'username': user.username,
            'points': user.points
        }
        return JsonResponse({'status':'success', 'message':'User retrieved', 'data' : userdata}, status = 201)

    
    def get(self, request):
        userlist = Users.objects.all()
        data = {}
        userlist = list(userlist.values('username', 'points'))
        for user in userlist:
            data.update({'username':user.username, 'points':user.points})
        return JsonResponse({'status':'success', 'message':'Users retrieved', 'data': data}, status = 200)
    
    def register(self, request):
        data = QueryDict(request.body.decode('utf-8'))
        form = UserCreateForm(data)
        if not form.is_valid():
            return JsonResponse({'status':'error', 'message':'Registration failed.'}, status = 400)
        user = form.save()
        login(request, user)
        pointsdata = {
            'username':data['username'],
            'points':0,
            'date_achieved':timezone.now
        }
        pointsform = PointsForm(pointsdata)
        if not pointsform.is_valid():
            return JsonResponse({'status':'error', 'message':'Registration failed.'}, status = 400)
        pointsform.save()
        userdata = {
            'username':data['username'],
            'points':0
        }
        return JsonResponse({'status':'success', 'message':'User registered successfully.', 'data': userdata}, status = 201)

    def login(self, request):
        data = QueryDict(request.body.decode('utf-8'))
        form = UserLoginForm(data)
        if not form.is_valid():
            return JsonResponse({'status': 'error', 'message': 'Login failed.'}, status=400)
        user = authenticate(
            request = request,
            username = data['username'],
            password = data['password']
        )
        if user is None:
            return JsonResponse({'status':'error', 'message':'User does not exist.'}, status = 400)

        login(request, user)
        userdata = {
            'username': user.username,
            'points': user.points
        }
        return JsonResponse({'status':'success', 'message':'User retrieved', 'data' : userdata}, status = 201)
        

    def logout(self, request):
        logout(request)
        return JsonResponse({'status': 'success', 'message': 'Logout successful'}, status=200)


class LeaderboardView(View):
    def post(self, request, *args, **kwargs):
        if 'add_points' in request.path:
            return self.add_points(request)
        elif 'update_points' in request.path:
            return self.update_points(request)
        return JsonResponse({'message':'Invalid request method.'}, status = 400)
    
    def get(self, request):
        pass

    def add_points(self, request):
        pass

    def update_points(self, request):
        data = json.loads(request.body)
        try:
            score = Leaderboard.objects.get(username = data['username'])
        except Leaderboard.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Leaderboard entry does not exist for player.'}, status=400)
        
        form = Leaderboard(data, instance = score)
        if not form.is_valid():
            return JsonResponse({'status': 'error', 'message': 'Score update failed.'}, status=400)
        
        score = form.save()
        user = Users.objects.get(username = data['username'])
        user.points = data['points']
        user.save()
        return JsonResponse({'status': 'success', 'message': 'Points updated successfully.'}, status = 201)
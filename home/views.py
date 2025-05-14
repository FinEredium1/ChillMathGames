from django.shortcuts import render

# Create your views here.


def index(request):
    template_data = {
        'username': request.user.username,
        'game_name': 'Ziggler',
    }
    return render(request, 'home/home.html', template_data)
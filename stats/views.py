from django.http import HttpResponse
from .models import Champion

def index(request):
    alphabetical = Champion.objects.order_by('-name')
    output = ', '.join([c.name for c in alphabetical])
    return HttpResponse(output)

def detail(request, champion_name):
    return HttpResponse("You're looking at details for %s." % champion_name)

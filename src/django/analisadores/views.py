from django.http import HttpResponse
from .classes import lexico

# Create your views here.
def resolve(request):
    if request.method == 'POST':
        string = request.POST.get()

        return HttpResponse(string)

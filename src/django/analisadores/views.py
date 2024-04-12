from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .classes import lexico

# Create your views here.
class Analise(View):
    def get(self, request):
        analisador_lexico = lexico.Lexic()

        try:
            analisador_lexico.check(request)
        except Exception as e:
            return HttpResponse(e)
    
        return HttpResponse('Sucesso')
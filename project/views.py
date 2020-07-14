import random

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import UniqueCode
# Create your views here.
# chat/views.py
from django.shortcuts import render
from .forms import UserNameForm

def index(request,pk):
    entered = False
    try:
        uniqueCode = UniqueCode.objects.get(uniqueCode=pk)
        sender = uniqueCode.sender
        try:
            if request.session['user']:
                pass
        except KeyError:
            uniqueCode.receiver = 'second player'
            entered = True
    except ObjectDoesNotExist:
        return HttpResponse("<h2>Doesn't Exist</h2>")
    return render(request, 'index.html',{'entered':entered,'sender':sender})
def createUniqueUrl(request):
    # generate code for url
    f = UserNameForm(request.POST or None)
    if request.POST:
        if f.is_valid():
            code = generateCode()
            f.save(code)
            request.session['user'] = f.cleaned_data['sender']
            return redirect('/game/'+str(code))
    return render(request,'enter.html',{'form':f})
def generateCode():
    return random.randint(0,2000)

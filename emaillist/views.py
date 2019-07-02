from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from emaillist.models import Emaillist


def main(request):
    emaillist = Emaillist.objects.all().order_by('-id')
    for t in emaillist:
        print(t)
    data = {
        'emaillist': emaillist
    }
    return render(request, 'emaillist/index.html', data)

def form(request):
    return render(request, 'emaillist/form.html')

def add(request):
    emaillist = Emaillist()
    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']
    emaillist.save()

    return HttpResponseRedirect('/emaillist')
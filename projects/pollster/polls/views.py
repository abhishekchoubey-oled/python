from django.shortcuts import render
from django.http import HttpResponse
from .models import Polls

# Create your views here.

def index(request) :
    #return HttpResponse('Hello from polls')
    polls = Polls.objects.all()[:10]
    context = {
        'title' : 'Latest Polls',
        'polls' : polls
    }
    return render(request, 'polls/index.html', context)
    #return render(request, 'polls/index.html', {'title':'Latest posts'}) ## this path is from inside the 'templates' directory in the 'polls' app
                                                ## it means the absolute path will look something like this 'project/polls/templates/polls/index.html


def detail(request, id) :
    poll = Polls.objects.get(id=id)
    context = {
        'poll' : poll
    }
    return render(request, 'polls/detail.html', context)

def page2(request) :
    return render(request, 'polls/page2.html')

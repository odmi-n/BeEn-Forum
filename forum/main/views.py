from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    TOPIC_LIST = Topic.objects.all()
    context = {
        "topics": TOPIC_LIST,
    }
    return render(request, "main/index.html", context)


def forum(request):
    pass

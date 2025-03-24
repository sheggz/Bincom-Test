from django.shortcuts import render
from .models import video
# Create your views here.

def home(request):
    if request.method == "GET":
        # retrieve all videos we have
        retreived_videos=video.objects.all()
        context = {"vids": retreived_videos}
    return render(request, "home.html", context=context)
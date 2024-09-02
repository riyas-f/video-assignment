
from django.shortcuts import render, redirect

from .models import Video

def upload_video(request):
    if request.method == 'POST':
        title = request.POST['title']
        file = request.FILES['file']

        video = Video.objects.create(title=title, file_path=file)
        return redirect('video_list')

    return render(request, 'videos/upload.html')

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from .models import Books, Comments, Audio

def record(request):
    return  render(request, 'record.html')

def books(request):
    allbooks = Books.objects.all()
    allaudios = Audio.objects.all()
    return render(request,'stories.html',{'allbooks': allbooks, 'allaudios': allaudios})

def read(request,id):
    vi = Books.objects.filter(id = id)[0]
    comments = Comments.objects.filter(post = vi)

    context = {'vi':vi, 'comments': comments, 'user': request.user}
    return render(request, "view.html", context)

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get("postSno")
        post = Books.objects.get(id=postSno)
        comment = Comments(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
    return redirect(f"/all/read/{post.id}")


def upload(request):
    thank = False
    if request.method == "POST":
        # user = request.user
        imgs = request.FILES.get('imgs')
        book_name = request.POST.get('book_name')
        book_desc = request.POST.get('book_desc')
        # fs = FileSystemStorage()
        # fs.save(img.name, img)
        profile = Books( img=imgs, book_desc=book_desc, book_name=book_name)
        profile.save()
        messages.add_message(request, messages.SUCCESS, "Successfully Uploaded")

        thank = True
    return render(request, 'upload.html')

def audio(request):
    if request.method == "POST":
        user = request.user
        story_audio = request.FILES['story_audio']
        story_name = request.POST.get('story_name')
        fa = FileSystemStorage()
        fa.save(story_audio.name, story_audio)
        profile = Audio(user=user, story_name = story_name, story_audio=story_audio)
        profile.save()
        messages.add_message(request, messages.SUCCESS, "Successfully Uploaded")


    return render(request, 'audiobook.html')

def audioplay(request,id):
    ai = Audio.objects.filter(id = id)[0]
    # comments = Comments.objects.filter(post = vi)

    context = {'ai':ai, 'user': request.user}
    return render(request, "audios.html", context)

from django.core import paginator
from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    diarys = Diary.objects.all()
    # 3장씩 출력하기
    paginator = Paginator(diarys, 3)
    page = request.GET.get('page')
    diarys = paginator.get_page(page)
    return render(request, 'home.html', {'diarys':diarys})

def detail(request, id):
    diary = get_object_or_404(Diary, pk=id)
    return render(request, 'detail.html', {'diary':diary})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_diary = Diary()
    new_diary.title = request.POST['title']
    new_diary.weather = request.POST['weather']
    new_diary.body = request.POST['body']
    new_diary.image = request.FILES['image']
    new_diary.pub_date = timezone.now()
    new_diary.save()
    return redirect('home')

def delete(request, id):
    delete_diary = Diary.objects.get(id = id)
    delete_diary.delete()
    return redirect('home')

def search(request):
    diarys = Diary.objects.all()
    search_text = request.GET.get('search_text')
    if search_text:
        diarys = diarys.filter(title__icontains = search_text)
        return render(request, 'search.html', {'diarys':diarys, 'search_text':search_text})
    return render(request, 'search.html', {'diarys':diarys, 'search_text':search_text})


def list(request):
    diarys = Diary.objects.all()
    # 3장씩 출력하기
    paginator = Paginator(diarys, 3)
    page = request.GET.get('page')
    diarys = paginator.get_page(page)
    return render(request, 'home.html', {'diarys':diarys})
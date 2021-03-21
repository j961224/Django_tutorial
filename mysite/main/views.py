from django.shortcuts import render
from .models import Cafe

def index(request): #사용자에게 request를 받으면 index.html로 연결
    cafelist = Cafe.objects.all()
    return render(request,'main/index.html',{'cafelist':cafelist})
    #cafelist라는 이름으로 전체 object를 index.html로 접근 가능
    
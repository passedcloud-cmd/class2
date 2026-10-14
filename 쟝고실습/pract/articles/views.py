from django.shortcuts import render

# Create your views here.
def index(request):
    context ={
        'name': 'Jane'
    }
    return render(request, 'articles/index.html', context)

import random
def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육']
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('query')
    context = {
        'data': message,
    }
    return render(request, 'articles/catch.html', context)

# urlpatterns에 있는 <int:num>을 받아온 것
# path converter의 변수명과 View함수의 파라미터 이름은 같아야 함.
def detail(request, num):
    context = {
        'num': num
    }
    return render(request, 'articles/detail.html', context)

def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/greeting.html', context)
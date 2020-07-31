from django.shortcuts import render, redirect
from .models import Board

# Create your views here.
def home(reqeust):
    return render(reqeust, "main/home.html")

# Create 방식 
# get 방식 ==> 글을 써서 그냥 보여주는 방식
# post 방식 ==> 편지 봉투에 넣고 보내주는 방식 (보안성 up)
# 1.html 내의 input 태그를 이용해 데이터를 받아와서 모델에 집어 넣기
# request(요청) 데이터를 받아오는 방식 
# ==> 요청과 함께 묶어서 데이터를 받아옴 ==> 요청에 데이터가 들어있다!!


def create_board(reqeust):
    # reqeust.POST["title"] ==> <input type="text" id="title" name="title"> 안의 데이터 불러옴
    title = reqeust.POST["title"]
    # reqeust.POST["author"] ==> <input type="text" id="title" name="author"> 안의 데이터 불러옴
    author = reqeust.POST["author"]
    # reqeust.POST["content"]==> <textarea id="title" name="contnet"><textarea/> 안의 데이터 불러옴
    contnet = reqeust.POST["content"]
    board = Board(title=title, author=author, content=contnet)
    # 데이터 베이스에 저장
    board.save()
    # 다른 방식
    # Board.objects.create(title=title, author=author, content=contnet)

    # url 하나에 하나의 html 만 보여주는 걸 권장
    # redirect ==> 지정된 url 로 보내주는 역할
    # path('', views.home, name="home"),
    # rediect('home')  ==> name="home" 인 path로 url 설정
    return redirect('home')

# 전체 게시글 보여주기
def read_board(request):
    # Board          /        .objects   /  .all()
    # Board 라는 모델/ 안에 있는 object 를/ 다 가져온다.
    boards = Board.objects.all()
    # 문자열 boards를 통해 위에서 가져온 데이터를 식별한다.
    # 딕셔너리 형태 ==> {key : value, 키 : 값}
    context = {'boards':boards}
    return render(request, "main/read.html", context)

# 게시글 하나 보여주기
def read_detail(request, pk):
    # Board/.objects/.get(조건=조건)
    # Board 라는 모델의/ object들 중/ 조건에 충족하는 것 하나만 가져오겠다
    board = Board.objects.get(pk=pk)
    context = {'board':board}
    return render(request, "main/detail_read.html", context)



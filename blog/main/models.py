from django.db import models
# 쓰는 이유 : auto_now 사용 -> admin page에서 임의적으로 수정불가
# 따라서 timezone 사용
from django.utils import timezone

# Create your models here.

# class = 붕어빵 틀 느낌~, 객체는 붕어빵
class Board(models.Model):
    # 제목, 저자 => 문자필드 ==> 데이터를 받을 때 문자로 받는다 (근데 최대길이 제한)
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=10)
    # 콘텐츠 => 긴문장 필드 ==> 유동적으로 데이터 저장 다 이걸로 안쓰는 이유 저장공간
    # 차지를 많이해서 서버속도가 느려질 수 있음
    content = models.TextField()
    # 생성시간 => 날짜필드 ==> default timezone.now ==> 현재시간을 기본으로 저장
    create_at = models.DateTimeField(default=timezone.now)

# 모델 변경을 많이 하지 않은 이유 ==> 기존 데이터가 날라거나 변형될 수 있다.
# 질문 이민호 : 모델 임포트 어디에 있는 거냐? 
# 대답: myvenv/lib/django/utils/timezone 에 있습니다.
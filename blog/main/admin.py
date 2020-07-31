from django.contrib import admin
from .models import Board

# import * => models 안에 있는 모델을 다 불러온다
# from .models import *

# Register your models here.
admin.site.register(Board)

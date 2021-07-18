from django.contrib import admin
from .models import Diary

# Diary 모델을 admin에 등록하기
admin.site.register(Diary)
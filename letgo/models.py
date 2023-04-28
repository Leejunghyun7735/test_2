from django.db import models

# Create your models here.
class Letgo(models.Model): #class상속
    title = models.CharField(max_length=100)
    content = models.TextField(null = True, blank = True)
    created_at = models.DateField(auto_now_add=True) #생성
    updated_at = models.DateField(auto_now=True) # 업데이트


    #1. 여기서 내가  class 상속을 했고 letgo라는 앱을 만들었다. 그러면 어디에다가 app을 추가해야되는지 생각해보자.
    def __str__(self):
        return str(self.title)
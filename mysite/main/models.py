from django.db import models

class Cafe(models.Model): #cafe 찾기
    name = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True) # 언제 퍼블리싱 됐는지
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Info(models.Model):
    id = models.AutoField(name='id', primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(name='url', max_length=15)
    about = models.TextField(name='about', max_length=120, blank=False, null=True)
    readonly_fields = ['id']
    def __str__(self):
        return f"[id: {self.id}] {self.user.username}"
    
    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'
    

class Post(models.Model):
    pub_date = models.DateTimeField(name="date")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(name="name", max_length=48)
    text = models.TextField(name="text", max_length=16192)
    
    def __str__(self):
        return f"[Name: {self.name}] {self.author.username}"
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
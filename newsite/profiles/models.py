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
    

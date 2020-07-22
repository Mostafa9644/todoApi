from django.db import models
from django.conf import settings

class Task(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False,blank=True,null=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.title

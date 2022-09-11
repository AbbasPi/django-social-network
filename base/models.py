from django.db import models
from django.contrib.auth.models import User
class BaseModel(models.Model):
    class Meta:
        abstract = True
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    
        
class Topic(BaseModel):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.name)


class Room(BaseModel):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants =
    
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return str(self.name)
    
    
class Message(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return str(self.content)
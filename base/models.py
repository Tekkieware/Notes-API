from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=400, null=False, blank=False)
    content = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)
    
    #Listing notes in their order of creation.
    class Meta:
        ordering = ['created_at']
    #Returning a title whenever an object of the model is called.
    def __str__(self):
        return self.title

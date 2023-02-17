from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=400, null=False, blank=False)
    content = models.TextField(null=True, blank=True)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

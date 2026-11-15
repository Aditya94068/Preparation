from django.db import models

class Task(models.Model):
    mark_as_completed = models.BooleanField(default=False)
    name =  models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
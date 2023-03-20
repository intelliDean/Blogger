from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author')

    # def __str__(self):
    #     return self.title

    def __str__(self):
        return self.created_at, self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])



from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, related_name='notes')
    content = models.TextField('content')
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created',]

    @classmethod
    def create(cls, user, content):
        cls.objects.create(user=user, content=content)


from django.db import models

class Room(models.Model):
    roomname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.roomname

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sender = models.CharField(max_length=255)
    def __str__(self):
        return self.message


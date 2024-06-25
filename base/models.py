from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE, null=True)
    receiver = models.CharField(max_length=100, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def delete_content(self):
        self.content = ''
        self.save() 

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField()
    image = models.ImageField(upload_to='images/', default="")
    created_at = models.DateTimeField(auto_now_add=True)
    reactions = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"

    def count_likes(self):
        return self.reactions.count()

    def add_reaction(self, user):
          if user in self.reactions.all():
            self.reactions.remove(user)
            action = "removed"
          else:
            self.reactions.add(user)
            action = "added"

        # Log the reaction history
          ReactionHistory.objects.create(
            user=user,
            post=self,
            reacted_at=timezone.now(),
            action=action
        )
    
    def get_likes(self):
        return self.reactions.all()
    
    
class ReactionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reacted_at = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=10)  # "added" or "removed"

    def __str__(self):
        return f"{self.user.username} {self.action} reaction on {self.post.id} at {self.reacted_at}"  

 


from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    content = models.CharField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default="0")

    def __str__(self):
        return f"Post {self.id} made by {self.user} on {self.date.strftime('%d %b %Y %H:%M:%S')} has {self.likes} like(s)"
    
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_who_is_following")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_who_is_being_followed")

    def __str__(self):
        return f"{self.follower} is following {self.following}"
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_like")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_like")

    def __str__(self):
        return f"{self.user} liked Post {self.post.id} made by {self.post.user} on {self.post.date.strftime('%d %b %Y %H:%M:%S')} which now has {self.post.likes} like(s)"
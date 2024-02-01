from django.db import models
from users.models import CustomUser as User

from utils.models import BaseModel

class Thread(BaseModel):
    """
    This model is used to hold post threads
    """
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class Post(BaseModel):
    """
    This model holds posted messages
    """
    thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE)
    message = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
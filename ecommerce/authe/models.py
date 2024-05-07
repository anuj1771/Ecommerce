from django.db import models
from django.contrib.auth.models import User
import uuid
 
class User(models.Model):
    User_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    def __int__(self):
        return self.id

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):

    is_admin = models.BooleanField('Administrateur', default=False)
    is_professeur = models.BooleanField('Professeur', default=True)
    photo = models.ImageField("Avatar", upload_to='user_profile',  blank = True)
    bannierer = models.ImageField("Bannière", upload_to='user_banner',  blank = True)
    is_first_connection = models.BooleanField(default = True)

   
from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, unique=True,
                                    error_messages={'unique':"Mobile number already exists"})
    
    is_manager = models.BooleanField('is manager', default=False)
    is_customer = models.BooleanField('is customer', default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()


    class Meta:
        db_table = 'user_user'
        verbose_name = 'user'
        verbose_name_plural ='users'
        ordering = ["-id"]

    def __str__(self):
        return self.phone_number
    

    
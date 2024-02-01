from django.db import models
from users.models import User


class Manager(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'manager_manager'
        verbose_name = 'manager'
        verbose_name_plural ='managers'
        ordering = ["-id"]


    def __str__(self):
        return self.user.phone_number
    

    
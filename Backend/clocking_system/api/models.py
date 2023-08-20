from django.db import models
from users.models import CustomUser


class Signing(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    clock_in_time = models.DateTimeField(auto_now_add=True)
    clock_out_time = models.DateTimeField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    
    @property
    def has_clocked_out(self):
        return self.clock_out_time is not None

    def __str__(self):
        return f"{self.user.username}"
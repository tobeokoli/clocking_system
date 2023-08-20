from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.email
    
    def time_worked_this_month(user):
        current_month = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        next_month = (current_month + timedelta(days=32)).replace(day=1)

        from api.models import Signing
        user_signings = Signing.objects.filter(
            user=user,
            date__gte=current_month,
            date__lt=next_month,
            clock_out_time__isnull=False
        )

        total_time = timedelta()
        for signing in user_signings:
            if signing.clock_out_time:
                total_time += signing.clock_out_time - signing.clock_in_time
        
        return total_time
    
    def salary_so_far_this_month(self):
        time_worked = self.time_worked_this_month()
        total_hours = time_worked.seconds // 3600
        # asumming a user is only paid full salary for 160hours of work in a month
        salary_so_far = (total_hours * self.salary) / 160
        return salary_so_far
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Only hash password if it's a new instance
            self.set_password(self.password)
        return super().save(*args, **kwargs)
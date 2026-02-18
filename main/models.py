from django.db import models
from django.utils import timezone

class InstagramLogin(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=255)
    login_time = models.DateTimeField(default=timezone.now)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    success = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-login_time']
        verbose_name = 'Instagram Login'
        verbose_name_plural = 'Instagram Logins'
    
    def __str__(self):
        return f"{self.username} - {self.login_time.strftime('%Y-%m-%d %H:%M')}"
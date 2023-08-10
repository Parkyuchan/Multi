from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(UserAdmin):
    # 관리자 화면에 보여질 칼럼 지정
    list_display = ("username", "email", "old", "phone", "address", "volunteer")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "email", "phone", "volunteer")
    ordering = ("username",)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'old', 'phone', 'address', 'email', 'volunteer')
            }
        ),
    )
    fieldsets = (
        ('Personal info', {'fields': ('username', 'password', 'old', 'phone', 'address', 'email', 'volunteer')}),
    )

admin.site.register(User, UserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from articles.admin import ArticleInline
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'age', 'is_staff']
    inlines = [
        ArticleInline,
    ]


admin.site.register(CustomUser, CustomUserAdmin)

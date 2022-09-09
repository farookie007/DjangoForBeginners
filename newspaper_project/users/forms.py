from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'age',)   # note that the addition is a tuple


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email', 'age',)
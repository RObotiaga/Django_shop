from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'phone', 'country', 'avatar')


class CustomUserUpdateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('phone', 'country', 'avatar')

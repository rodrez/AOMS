from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import AomsUser


class AomsUserCreationForm(UserCreationForm):
    class Meta:
        model = AomsUser
        fields = ("email",)


class AomsUserChangeForm(UserChangeForm):
    class Meta:
        model = AomsUser
        fields = ("email",)

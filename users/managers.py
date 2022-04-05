from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class AomsUserManager(BaseUserManager):

    """
    This custom user model manager uses email as the unique identifier instead of the username for auth.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and Saves an User with the given email and password

        Parameters
        ----------
        email : str
            Email for the user account
        password : str
            Password for the user account
        """

        if not email:
            raise ValueError(_("Email must be set"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and Saves an SuperUser with the given email and password

        Parameters
        ----------
        email : str
            Email for the user account
        password : str
            Password for the user account
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_supesuser=True."))

        return self.create_user(email, password, **extra_fields)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportMixin

from .forms import AomsUserChangeForm, AomsUserCreationForm
from .models import AomsUser


class AomsUserAdmin(ImportExportMixin, UserAdmin):

    add_form = AomsUserCreationForm
    form = AomsUserChangeForm
    model = AomsUser
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(AomsUser, AomsUserAdmin)

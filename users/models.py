from datetime import timezone

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """User Model"""

    email = models.EmailField(unique=True, max_length=255, blank=False)
    first_name = models.CharField(_('First Name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=30, blank=True)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('Designates whether this user should be '
                    'treated as active. Unselect this instead '
                    'of deleting accounts.'
                    )
    )
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    last_updated = models.DateTimeField(_('last updated'), auto_now=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'


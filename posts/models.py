from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Posts(models.Model):
    image_path = models.TextField(verbose_name=_('image path'))
    description = models.TextField(verbose_name=_('description'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    modified = models.DateTimeField(auto_now=True, verbose_name=_('modified'))

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        ordering = ['-created']
        verbose_name = _('post')
        verbose_name_plural = _('posts')

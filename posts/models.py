from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Posts(models.Model):
    image = models.URLField(verbose_name=_('image'), max_length=350)
    description = models.TextField(verbose_name=_('description'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'), null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    modified = models.DateTimeField(auto_now=True, verbose_name=_('modified'))

    def __str__(self):
        return f'{self.user.get_full_name()}'

    class Meta:
        ordering = ['-created']
        verbose_name = _('post')
        verbose_name_plural = _('posts')

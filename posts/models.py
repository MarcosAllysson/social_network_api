import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


def get_file_path(_, filename):
    file_extension = filename.split('.')[-1]
    filename = f'posts/{uuid.uuid4()}.{file_extension}'
    return filename


class Posts(models.Model):
    image = models.ImageField(upload_to=get_file_path, verbose_name=_('image'))
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

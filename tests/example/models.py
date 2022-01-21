from django.utils.translation import gettext_lazy as _
from django.db import models

from file_field_utils.db.fields import SVGAndImageField
from file_field_utils.db.utils.backend import UploadPath


class News(models.Model):
    title = models.CharField(_("Title"), max_length=64, )
    image = SVGAndImageField(_("Image"), upload_to=UploadPath(""), blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

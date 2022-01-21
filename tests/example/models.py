from django.db import models
from django.utils.translation import gettext_lazy as _

from file_field_utils.db.fields import SVGAndImageField
from file_field_utils.db.utils.backend import UploadPath, UploadPathWithID


class News(models.Model):
    title = models.CharField(
        _("Title"),
        max_length=64,
    )
    image = SVGAndImageField(_("Image"), upload_to=UploadPath(""), blank=True)
    image_1 = SVGAndImageField(
        _("Image 1"), upload_to=UploadPath("example_dir"), blank=True
    )
    image_2 = SVGAndImageField(_("Image 2"), upload_to=UploadPathWithID(""), blank=True)
    image_3 = SVGAndImageField(
        _("Image 3"), upload_to=UploadPathWithID("example_dir"), blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

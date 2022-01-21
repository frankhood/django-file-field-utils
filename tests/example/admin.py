from django.contrib import admin

from file_field_utils.db.widgets import ConfigurableImageWidget
from tests.example.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    dbfield_overrides = {
        "image": {"widget": ConfigurableImageWidget()},
    }

    def formfield_for_dbfield(self, db_field, request=None, **kwargs):
        if (self.dbfield_overrides and
                db_field.name in self.dbfield_overrides):
            kwargs.update(
                self.dbfield_overrides[db_field.name]
            )
        return super(NewsAdmin, self).formfield_for_dbfield(
            db_field, request, **kwargs)

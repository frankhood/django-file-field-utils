from unittest import TestCase

import svgwrite
from django.contrib.admin import AdminSite
from django.core.files.uploadedfile import SimpleUploadedFile

from file_field_utils.db.widgets import ConfigurableImageWidget
from tests.example.admin import NewsAdmin
from tests.example.models import News


class MockRequest:
   pass


class MockSuperUser:
   def has_perm(self, perm, obj=None):
       return True


request = MockRequest()
request.user = MockSuperUser()

class AdminTest(TestCase):

    # =======================================================================
    # ./manage.py test tests.test_admin.AdminTest  --settings=tests.settings
    # =======================================================================

    import platform
    print(platform.python_version())

    def setUp(self):
        self.site = AdminSite()

    # =======================================================================
    # ./manage.py test tests.test_admin.AdminTest.test_image_in_admin_fields  --settings=tests.settings
    # =======================================================================
    def test_image_in_admin_fields(self):

        admin = NewsAdmin(News, self.site)
        fields = admin.get_fields(request=None)

        self.assertIn("image", fields)

    # =======================================================================
    # ./manage.py test tests.test_admin.AdminTest.test_image_is_ConfigurableImageWidget  --settings=tests.settings
    # =======================================================================
    def test_image_is_ConfigurableImageWidget(self):

        admin = NewsAdmin(News, '')
        form = admin.get_form(None)

        self.assertIn('image', form.base_fields)

        image_field = form.base_fields.get("image")
        self.assertIsInstance(image_field.widget, ConfigurableImageWidget)

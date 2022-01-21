import shutil
from unittest import TestCase

from PIL import Image
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from six import BytesIO

from tests.example.models import News


class StorageTest(TestCase):
    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        News.objects.all().delete()
        shutil.rmtree("uploads")
    # =======================================================================
    # python manage.py test tests.test_storage.StorageTest  --settings=tests.settings
    # =======================================================================

    # =======================================================================
    # python manage.py test tests.test_storage.StorageTest.test_create_image_in_UploadPath  --settings=tests.settings
    # =======================================================================
    def test_create_image_in_UploadPath(self):
        # -----------------
        data = BytesIO()
        size = (100, 100)
        image_mode = 'RGB'
        image_format = 'PNG'
        file_name = "myimage.png"
        Image.new(image_mode, size).save(data, image_format)
        data.seek(0)
        image_file = ContentFile(data.read(), file_name)
        # -----------------
        news = News.objects.create(
            title="my_news",
            image=image_file
        )

        formfield = news.image.field.formfield()
        formfield.run_validators(news.image)
        try:
            self.assertEqual(news.image.url, f"/uploads/{news._meta.app_label}/{news._meta.model_name}/{file_name}")
        except AssertionError:
            # python 3.6 django 2.2
            self.assertIn(news.image.url, f"/uploads/{news._meta.app_label}/{news._meta.model_name}/{file_name}")


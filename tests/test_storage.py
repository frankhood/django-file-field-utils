import shutil

from django.core.files.base import ContentFile
from django.test import TestCase
from PIL import Image
from urllib3.packages.six import BytesIO

from tests.example.models import News


class StorageTest(TestCase):
    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        shutil.rmtree("uploads")

    # =======================================================================
    # python manage.py test tests.test_storage.StorageTest  --settings=tests.settings
    # =======================================================================

    # =======================================================================
    # python manage.py test tests.test_storage.StorageTest.test_create_image_in_UploadPath_default  --settings=tests.settings
    # =======================================================================
    def test_create_image_in_UploadPath_default(self):
        # -----------------
        data = BytesIO()
        size = (100, 100)
        image_mode = "RGB"
        image_format = "PNG"
        file_name = "myimage.png"
        Image.new(image_mode, size).save(data, image_format)
        data.seek(0)
        image_file = ContentFile(data.read(), file_name)
        # -----------------
        news = News.objects.create(title="my_news", image=image_file)

        formfield = news.image.field.formfield()
        formfield.run_validators(news.image)
        try:
            self.assertEqual(
                news.image.url,
                f"/uploads/{news._meta.app_label}/{news._meta.model_name}/{file_name}",
            )
        except AssertionError:
            # python 3.6 django 2.2
            self.assertIn(
                news.image.url,
                f"/uploads/{news._meta.app_label}/{news._meta.model_name}/{file_name}",
            )

    # =======================================================================
    # python manage.py test tests.test_storage.StorageTest.test_create_image_in_UploadPath_with_parameter  --settings=tests.settings
    # =======================================================================
    def test_create_image_in_UploadPath_with_parameter(self):
        # -----------------
        data = BytesIO()
        size = (100, 100)
        image_mode = "RGB"
        image_format = "PNG"
        file_name = "myimage.png"
        Image.new(image_mode, size).save(data, image_format)
        data.seek(0)
        image_file = ContentFile(data.read(), file_name)
        # -----------------
        news = News.objects.create(title="my_news", image_1=image_file)

        formfield = news.image_1.field.formfield()
        formfield.run_validators(news.image_1)
        try:
            self.assertEqual(
                news.image_1.url,
                f"/uploads/{news._meta.app_label}/{news._meta.model_name}/example_dir/{file_name}",
            )
        except AssertionError:
            # python 3.6 django 2.2
            self.assertIn(
                news.image_1.url,
                f"/uploads/{news._meta.app_label}/{news._meta.model_name}/example_dir/{file_name}",
            )

    # =======================================================================
    # python manage.py test tests.test_storage.StorageTest.test_create_image_in_UploadPathWithID_default  --settings=tests.settings
    # =======================================================================
    def test_create_image_in_UploadPathWithID_default(self):
        # -----------------
        data = BytesIO()
        size = (100, 100)
        image_mode = "RGB"
        image_format = "PNG"
        file_name = "myimage.png"
        Image.new(image_mode, size).save(data, image_format)
        data.seek(0)
        image_file = ContentFile(data.read(), file_name)
        # -----------------
        news = News.objects.create(
            title="my_news",
        )
        news.image_2 = image_file
        news.save()

        formfield = news.image_2.field.formfield()
        formfield.run_validators(news.image_2)
        try:
            self.assertEqual(
                news.image_2.url,
                f"/uploads/{news._meta.app_label}/{news._meta.model_name}/{news.id}/{file_name}",
            )
        except AssertionError:
            # python 3.6 django 2.2
            self.assertIn(
                news.image_2.url,
                f"/uploads/{news._meta.app_label}/{news._meta.model_name}/{news.id}/{file_name}",
            )

    # =======================================================================
    # python manage.py test tests.test_storage.StorageTest.test_create_image_in_UploadPathWithID_with_parameter  --settings=tests.settings
    # =======================================================================
    def test_create_image_in_UploadPathWithID_with_parameter(self):
        # -----------------
        data = BytesIO()
        size = (100, 100)
        image_mode = "RGB"
        image_format = "PNG"
        file_name = "myimage.png"
        Image.new(image_mode, size).save(data, image_format)
        data.seek(0)
        image_file = ContentFile(data.read(), file_name)
        # -----------------
        news = News.objects.create(
            title="my_news",
        )
        news.image_3 = image_file
        news.save()

        formfield = news.image_3.field.formfield()
        formfield.run_validators(news.image_3)
        try:
            self.assertEqual(
                news.image_3.url,
                f"/uploads/{news._meta.app_label}/{news._meta.model_name}/example_dir/{news.id}/{file_name}",
            )
        except AssertionError:
            # python 3.6 django 2.2
            self.assertIn(
                news.image_3.url,
                f"/uploads/{news._meta.app_label}/{news._meta.model_name}/example_dir/{news.id}/{file_name}",
            )

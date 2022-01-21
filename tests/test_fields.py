import os
import shutil
import tempfile
from unittest import TestCase

import svgwrite
from PIL import Image
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from six import BytesIO

from file_field_utils.db.fields import SVGAndImageField
from tests.example.models import News


class FieldTest(TestCase):

    # =======================================================================
    # python manage.py test tests.test_fields.FieldTest  --settings=tests.settings
    # =======================================================================

    import platform
    print(platform.python_version())
    #
    # def setUp(self):
    #     self.site = AdminSite()

    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        News.objects.all().delete()
        shutil.rmtree("uploads")


    # =======================================================================
    # python manage.py test tests.test_fields.FieldTest.test_create_SVGAndImageField_with_svg_SUCCESS  --settings=tests.settings
    # =======================================================================
    def test_create_SVGAndImageField_with_svg_SUCCESS(self):
        #-----------------
        svg_document = svgwrite.Drawing(filename="test-svgwrite.svg",
                                        size=("800px", "600px"))
        svg_document.add(svg_document.rect(insert=(0, 0),
                                           size=("200px", "100px"),
                                           stroke_width="1",
                                           stroke="black",
                                           fill="rgb(255,255,0)"))
        svg_document.add(svg_document.text("Hello World",
                                           insert=(210, 110)))
        svg_document.save()
        #-----------------
        news = News.objects.create(
            title="my_news",
            image=SimpleUploadedFile(name='test_image.svg', content=open(svg_document.filename, 'rb').read(),)
        )

        formfield = news.image.field.formfield()
        # with self.assertRaises(ValidationError):
        formfield.run_validators(news.image)
        self.assertIsInstance(news.image.field, SVGAndImageField)
        self.assertEqual(News.objects.count(), 1)
        os.remove("test-svgwrite.svg")


    # =======================================================================
    # python manage.py test tests.test_fields.FieldTest.test_create_SVGAndImageField_with_doc_validation_FAIL  --settings=tests.settings
    # =======================================================================
    def test_create_SVGAndImageField_with_doc_validation_FAIL(self):
        #-----------------
        svg_document = svgwrite.Drawing(filename="test-svgwrite.svg",
                                        size=("800px", "600px"))
        svg_document.add(svg_document.rect(insert=(0, 0),
                                           size=("200px", "100px"),
                                           stroke_width="1",
                                           stroke="black",
                                           fill="rgb(255,255,0)"))
        svg_document.add(svg_document.text("Hello World",
                                           insert=(210, 110)))
        svg_document.save()
        #-----------------
        news = News.objects.create(
            title="my_news",
            image=SimpleUploadedFile(name='test_image.doc', content=open(svg_document.filename, 'rb').read(),)
        )

        formfield = news.image.field.formfield()
        with self.assertRaises(ValidationError):
            formfield.run_validators(news.image)
        self.assertEqual(News.objects.count(), 1)
        os.remove("test-svgwrite.svg")

    # =======================================================================
    # python manage.py test tests.test_fields.FieldTest.test_create_SVGAndImageField_with_png_SUCCESS  --settings=tests.settings
    # =======================================================================
    def test_create_SVGAndImageField_with_png_SUCCESS(self):
        #-----------------
        data = BytesIO()
        size = (100, 100)
        image_mode = 'RGB'
        image_format = 'PNG'
        file_name = "myimage.png"
        Image.new(image_mode, size).save(data, image_format)
        data.seek(0)
        image_file = ContentFile(data.read(), file_name)
        #-----------------
        news = News.objects.create(
            title="my_news",
            image=image_file
        )

        formfield = news.image.field.formfield()
        formfield.run_validators(news.image)
        self.assertIsInstance(news.image.field, SVGAndImageField)
        self.assertEqual(News.objects.count(), 1)



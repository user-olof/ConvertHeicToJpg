import pillow_heif
from pillow_heif import HeifImage
import pytest
# import unittest
# import cv2
from io import BytesIO
from PIL import Image
import os
import imghdr
from pyfakefs.fake_filesystem_unittest import TestCase

class TestConvertToJpeg(TestCase):
    def setUp(self):
        self.setUpPyfakefs()

    def test_create_file(self):
        # "fs" is the reference to the fake file system
        # file_path = "/tests/xxx.txt"
        img = self.create_png_image()
        self.assertTrue(img.format == 'png')
        file_path = r'/tests/' + img.name
        heif = self.create_test_image(img)
        x = os.path.abspath(heif)
        self.assertFalse(os.path.exists(file_path))
        self.fs.create_file(file_path)
        print('\n\r' + os.path.abspath(file_path))
        self.assertTrue(os.path.exists(file_path))
        
        self.assertTrue(imghdr.what(file_path) == 'heif')
        print('\n\r' + imghdr.what(file_path))

    def create_png_image(self):
        buf = BytesIO()
        im = Image.new(mode='RGB', size=(50, 50), color=(155, 0, 0))
        im.save("test.jpg")
        buf.seek(0)
        return buf



    def create_test_image(self, fp):

        heif_file = pillow_heif.from_bytes(mode="BGRA;16",
                                           size=(fp.shape[1], fp.shape[0]),
                                           data=bytes(fp))
        if not pillow_heif.is_supported(heif_file):
            raise Exception('Image is not supported')

        return heif_file




    def test_create_dir(self, tmp_path):
        d = tmp_path / "sub"
        d.mkdir()
        assert len(list(tmp_path.iterdir())) == 1
        assert 0

    def test_convert_to_jpg(self):
        x = "hi"
        assert "h" in x
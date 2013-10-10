#!flask/bin/python

"""Image Resizer application unit tests."""

__author__ = "Carlos Gomez (carlosg24@gmail.com)"

import cStringIO

import app
import image_resizer
import unittest

from PIL import Image


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def testResizeRouteNoURL(self):
        response = self.app.get('/resize')
        self.assertEqual(response.data, app.NO_URL_ERROR_MESSAGE)

    def testResizeRouteNoWidthOrHeight(self):
        response = self.app.get('/resize', data=dict(
            url='http://localhost/image.jpg'))
        self.assertEqual(response.data, app.NO_URL_ERROR_MESSAGE)


class ImageResizerTests(unittest.TestCase):

    def setUp(self):
        self.test_image_resizer = image_resizer.ImageResizer()
        color = (0, 0, 255, 0)
        size = (400, 200)
        self.test_landscape_image = Image.new("RGBA", size, color)
        size = (200, 400)
        self.test_portrait_image = Image.new("RGBA", size, color)

    def testResizeImageFromURL(self):
        """Tests the resize_image_from_url method."""
        test_file = cStringIO.StringIO()
        self.test_landscape_image.save(test_file, format='jpeg')
        test_file.seek(0)
        real_StringIO = cStringIO.StringIO
        # Quick monkey-patch to mock out StringIO creation when an argument
        # is passed to constructor. Would use mocking library if needed
        # more mocking than this.
        cStringIO.StringIO = (lambda x=False:
                              test_file if x else real_StringIO())
        file, format = self.test_image_resizer.resize_image_from_url(
            'http://127.0.0.1/image.jpeg', 0, 0, False)
        cStringIO.StringIO = real_StringIO
        self.assertTrue(file)
        self.assertEqual('JPEG', format)

    def testResizeImageDontKeepAspect(self):
        """Tests the resize_image method with keep_aspect_ratio=False."""
        result_image = self.test_image_resizer.resize_image(
            self.test_landscape_image, 100, 150, False)
        self.assertEqual((100, 150), result_image.size)

    def testResizeImageNoWidth(self):
        """Tests resize_image method with width set to 0."""
        result_image = self.test_image_resizer.resize_image(
            self.test_landscape_image, 0, 150, False)
        self.assertEqual((400, 150), result_image.size)

    def testResizeImageNoHeight(self):
        """Tests resize_image method with height set to 0."""
        result_image = self.test_image_resizer.resize_image(
            self.test_landscape_image, 100, 0, False)
        self.assertEqual((100, 200), result_image.size)

    def testResizeLandscapeImageKeepAspect(self):
        """Tests a landscape image aspect ratio resize."""
        result_image = self.test_image_resizer.resize_image(
            self.test_landscape_image, 200, 150, True)
        self.assertEqual((200, 100), result_image.size)

    def testResizeLandscapeImageKeepAspectNoWidth(self):
        """Tests a landscape image aspect ratio resize with width set to 0."""
        result_image = self.test_image_resizer.resize_image(
            self.test_landscape_image, 0, 150, True)
        self.assertEqual((300, 150), result_image.size)

    def testResizeLandscapeImageKeepAspectNoHeight(self):
        """Tests a landscape image aspect ratio resize with height set to 0."""
        result_image = self.test_image_resizer.resize_image(
            self.test_landscape_image, 300, 0, True)
        self.assertEqual((300, 150), result_image.size)

    def testResizePortraitImageKeepAspect(self):
        """Tests a portrait image aspect ratio resize."""
        result_image = self.test_image_resizer.resize_image(
            self.test_portrait_image, 200, 150, True)
        self.assertEqual((75, 150), result_image.size)

    def testResizePortraitImageKeepAspectNoWidth(self):
        """Tests a portrait image aspect ratio resize with width set to 0."""
        result_image = self.test_image_resizer.resize_image(
            self.test_portrait_image, 0, 150, True)
        self.assertEqual((75, 150), result_image.size)

    def testResizePortraitImageKeepAspectNoHeight(self):
        """Tests a portrait image aspect ratio resize with height set to 0."""
        result_image = self.test_image_resizer.resize_image(
            self.test_portrait_image, 300, 0, True)
        self.assertEqual((300, 600), result_image.size)


if __name__ == '__main__':
    unittest.main()

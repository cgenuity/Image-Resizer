#!flask/bin/python

""" Image Resizer module. """

__author__ = "Carlos Gomez (carlosg24@gmail.com)"

import cStringIO
import urllib

from PIL import Image

RESIZED_IMAGE_QUALITY = 90


class ImageResizer(object):
    """Resizes images using the PILibrary."""
    def resize_image_from_url(self, url, width, height, keep_aspect_ratio):
        """Resizes an image in memory given a URL.

        Args:
            url: A string of the URL to fetch an image from.
            width: An integer of the width to resize the image to.
            height: An integer of the height to resize the image to.
            keep_aspect_ratio: A boolean of whether to keep the image's
                aspect ratio.

        Returns:
            A tuple of the image file and the image format.
        """
        # TODO(Carlos): Since this is done in memory, consider enforcing a file
        # size limit.

        # Depending on who will use this application, it might be good to
        # catch urlopen and Image.open errors and act accordingly.
        # Assuming users will be either me or someone similarly technical,
        # I'll let it throw errors to make it easier to debug.
        file = cStringIO.StringIO(urllib.urlopen(url).read())
        image = Image.open(file)
        resized_image = self.resize_image(image, width, height,
                                          keep_aspect_ratio)
        resized_file = cStringIO.StringIO()
        resized_image.save(resized_file, format=image.format,
                           quality=RESIZED_IMAGE_QUALITY)
        resized_file.seek(0)
        return resized_file, image.format

    def resize_image(self, image, width, height, keep_aspect_ratio):
        """Resizes a PIL image object.

        Args:
            image: A PIL image object.
            width: An integer of the width to resize the image to.
            height: An integer of the height to resize the image to.
            keep_aspect_ratio: A boolean of whether to keep the image's
                aspect ratio.

        Returns:
            The resized PIL image object.
        """
        original_width, original_height = image.size
        if keep_aspect_ratio:
            if original_width > original_height:  # Landscape image
                ratio = float(original_height)/float(original_width)
                if width:
                    height = int(float(width) * ratio)
                else:
                    width = int(float(height) / ratio)
            else:  # Portrait image
                ratio = float(original_width)/float(original_height)
                if height:
                    width = int(float(height) * ratio)
                else:
                    height = int(float(width) / ratio)
        else:
            if not width:
                width = original_width
            if not height:
                height = original_height
        resized_image = image.resize((width, height), Image.ANTIALIAS)
        return resized_image

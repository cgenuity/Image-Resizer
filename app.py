#!flask/bin/python

""" Image Resizer RESTful web application.

    A tiny RESTful web application with one resource that accepts a URL and
    some image dimensions, and returns an image resized to those dimensions.
"""

__author__ = "Carlos Gomez (carlosg24@gmail.com)"

from flask import Flask
from flask import request
from flask import send_file

from image_resizer import ImageResizer

URL_KEY = 'url'
WIDTH_KEY = 'width'
HEIGHT_KEY = 'height'
KEEP_ASPECT_RATIO_KEY = 'keep-aspect-ratio'

NO_URL_ERROR_MESSAGE = 'A URL is required.'
NO_WIDTH_OR_HEIGHT_ERROR_MESSAGE = 'A width or height (in pixels) is required.'

app = Flask(__name__)


@app.route('/resize', methods=['GET'])
def resize():
    """Defines the /resize endpoint.

       Responds to GET requests to /resize with the resized image.

       Accepted Parameters:
            url: URL of the image to resize.
            width: Width to resize the image to.
            height: Height to resize the image to.
            keep_aspect_ratio: A value of 'true' keeps the original aspect
                ratio.
    """
    url = request.args.get(URL_KEY, False)
    width = int(request.args.get(WIDTH_KEY, False))
    height = int(request.args.get(HEIGHT_KEY, False))
    keep_aspect_ratio = (True if request.args.get(KEEP_ASPECT_RATIO_KEY, False)
                         == 'true' else False)

    # Simple argument validation
    if not url:
        return NO_URL_ERROR_MESSAGE
    if not width and not height:
        return NO_WIDTH_OR_HEIGHT_ERROR_MESSAGE

    resizer = ImageResizer()
    resized_file, format = resizer.resize_image_from_url(url, width,
                                                         height,
                                                         keep_aspect_ratio)
    mimetype = 'image/' + format.lower()
    return send_file(resized_file, mimetype=mimetype)

if __name__ == '__main__':
    app.run(debug=True)

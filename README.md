## Image Resizer

Image resizer is a RESTful service with the sole purpose of resizing an image specified by a URL.

## Installation

Fork or download the source on a UNIX-based system and run **./app.py**. By default it will run a flask server on **http://localhost:5000/**. No other installation should be required since virtualenv was used to create an isolated environment.

## Example Usage

http://localhost:5000/resizer/url=http://i.imgur.com/9rSryrU.jpg&width=600&height=600&keep-aspect-ratio=true

## Tests

Tests can be run by running ./tests.py on a UNIX-based system.


## License


The MIT License (MIT)

Copyright (c) 2013 Carlos Gomez (carlos24@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


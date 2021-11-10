# pip install pillow

from PIL import Image

im = Image.open("static/cat2.jpg")
im.thumbnail((1200, 900))
im.save("static/cat2.jpg")
"""MemeGenerator uses Pillow library to create memes"""
import os
import textwrap
from random import random, randint

from PIL import Image, ImageDraw, ImageFont


class MemeGenerator:
    "Meme class"
    def __init__(self, output_dir):
        # method takes a required argument for where to save the generated images
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Make the meme."""
        img = Image.open(img_path)

        # Transform image by resizing to a maximum width of 500px while maintaining the input aspect ratio
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        scaled_img = img.resize((width, height))

        # add a quote body and quote author to the image & save manipulated image
        # Add a caption to an image (string input) with a body and author to a random location on the image.
        if text is not None:
            draw = ImageDraw.Draw(scaled_img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf',
                                        size=20)
            #draw.text((10, 10), f'"{text}" - {author}', font=font)
            #Adding text wrap with fill()method for very long text.
            wrapped_text = textwrap.fill(text=f"{text} - {author}")
            draw.text((10, 35), wrapped_text, font=font)
        rand_num = randint(0, 10000)
        out_file = os.path.join(self.output_dir, f'./{rand_num}.jpg')
        scaled_img.save(out_file)
        return out_file

    # add try-catch blocks for common exceptions

"""
The project defines a MemeGenerator module with the following responsibilities:

Loading of a file from disk
Transform image by resizing to a maximum width of 500px while maintaining the input aspect ratio
Add a caption to an image (string input) with a body and author to a random location on the image.

The class depends on the Pillow library to complete the defined, incomplete method signatures so that they work with JPEG/PNG files.
"""
import os
from random import random

from PIL import Image, ImageDraw, ImageFont


class MemeGenerator:
    def __init__(self, output_dir):
        # required argument for where to save the generated images
        self.output_dir = output_dir
        os.makedirs(self.output_dir)

    # def __str__(self) -> str:
    #    return f"{self.output_dir}"

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Make the meme."""
        img = Image.open(img_path)

        # resize image so the width is at most 500px and height scaled proportionally.
        if width > 500:
            width = 500
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            scaled_img = img.resize((width, height))

        # add a quote body and quote author to the image & save manipulated image
        if text is not None:
            draw = ImageDraw.Draw(scaled_img)
            font = ImageFont.truetype("arial.pil")  # use a bitmap font
            draw.text((10, 10), f'"{text}" - {author}', font=font)
        rand_num = random.randint(0, 1000)
        out_file = os.path.join(self.output_dir, f'./{rand_num}.jpg')
        scaled_img.save(out_file)
        return out_file

    # add try-catch blocks for common exceptions

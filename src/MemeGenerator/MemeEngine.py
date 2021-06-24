"""CVS Ingestor.

This script requires that the 'random', 'os', and 'PIL'
libraries be installed within the Python environment this script
is being run in.
"""

import random
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class MemeEngine:
    """A class used to manipulate and add text to an image.

    ...

    Methods:
        make_meme(img_path, text, author, width=500): Returns the
            str path to the meme image
    """

    def __init__(self, output_dir):
        """Return the str path to the output meme image.

        Arguments:
            output_dir{[str]}: the path where the final meme is located
        """
        output_dir = output_dir.replace('./', '')
        root = os.path.dirname(os.path.dirname(__file__))
        output_dir = os.path.join(root, output_dir+'/').replace('\\', '/')
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Return the str path to the output meme image.

        Arguments:
            img_path{[str]}: the path where the file to be read is located
            text{[str]}: body of the quote
            author{[str]}: author of the quote
            width{[int]}: width of the resized image
        Raises:
            Exception: if the file at the path is not of the correct format
                    or meme image cannot be modified
        """
        try:
            img = Image.open(img_path)
        except Exception as e:
            raise Exception("Input Image path is invalid")
        try:
            output_path = f"./static/meme_{random.randint(0, 255)}.jpg"
            save_path = os.path.join(self.output_dir,
                                     output_path.replace('./static/', ''))
            scale = width/img.size[1]
            height_scaled = int(scale*img.size[0])
            resized_img = img.resize((width, height_scaled))
            draw = ImageDraw.Draw(resized_img)
            txt = text + "\n-" + author
            root = os.path.dirname(__file__)
            path = os.path.join(root, "Arial.ttf").replace('\\', '/')
            font = ImageFont.truetype(path, 25)
            x = random.randint(10, 100)
            y = random.randint(10, height_scaled-60)
            draw.multiline_text((x, y), txt,
                                fill='white', stroke_fill='black', font=font)
            resized_img.save(save_path)
            return output_path
        except Exception as e:
            raise Exception("Problem with editing meme")

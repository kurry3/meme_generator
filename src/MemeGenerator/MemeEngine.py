import random
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class MemeEngine:
    def __init__(self, output_dir):
        output_dir = output_dir.replace('./', '')
        root = os.path.dirname(os.path.dirname(__file__))
        output_dir = os.path.join(root, output_dir+'/').replace('\\', '/')
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        try:
            output_path = f"./static/meme_{random.randint(0, 255)}.jpg"
            save_path = os.path.join(self.output_dir,
                                     output_path.replace('./static/', ''))
            img = Image.open(img_path)
            scale = width/img.size[1]
            resized_img = img.resize((width, int(scale*img.size[0])))
            draw = ImageDraw.Draw(resized_img)
            txt = text + "\n-" + author
            root = os.path.dirname(__file__)
            path = os.path.join(root, "Arial.ttf").replace('\\', '/')
            font = ImageFont.truetype(path, 25)
            draw.multiline_text((50, 50), txt,
                                fill='white', stroke_fill='black', font=font)
            resized_img.save(save_path)
            return output_path
        except Exception as e:
            raise Exception(e)

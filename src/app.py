import random
import os
import requests
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel
from MemeGenerator.MemeEngine import MemeEngine
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for quote in quote_files:
        quotes.extend(Ingestor.parse(quote))

    images_path = "./_data/photos/dog/"
    path = images_path.replace('./', '')
    root = os.path.dirname(__file__)
    images_path = os.path.join(root, path).replace('\\', '/')

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        for file_name in files:
            imgs.append(os.path.join(root, file_name))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form parameters.
    # 3. Remove the temporary saved image.

    img_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    tmp = f'/static/{random.randint(0, 255)}.png'
    root = os.path.dirname(__file__)
    tmp = os.path.join(root, tmp).replace('\\', '/')
    data = requests.get(img_url, stream=True).content
    with open(tmp, 'wb') as output_img:
        output_img.write(data)
    path = meme.make_meme(tmp, body, author)
    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()

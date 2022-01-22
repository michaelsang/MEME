import random
import os
import requests
from flask import Flask, render_template, abort, request

# import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor
from MemeEngine import MemeGenerator

app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the
    # https://knowledge.udacity.com/questions/643985

    # quote_files variable
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))


    images_path = "./_data/photos/dog/"

    # Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    img = random.choice(imgs)
    # 2. select a random quote from the quotes array
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

    #
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    image_url = requests.form['image_url']
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    body = request.form['body']
    author = request.form['author']
    req = requests.get(image_url, allow_redirects = True)
    temp_file = f'./{random.randint(0, 10000)}.jpg'
    open(temp_file,"wb").write(req.content)
    path = meme.make_meme(temp_file, body, author)
    # 3. Remove the temporary saved image.
    os.remove(temp_file)

    #path = None

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()

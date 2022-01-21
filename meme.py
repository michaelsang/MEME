import argparse
import os
import random

# Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeGenerator


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None: # path argument is list
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0] # if path is string get first character

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeGenerator('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # Use ArgumentParser to parse the following CLI arguments
    parser = argparse.ArgumentParser(description='gives a meme')

    # path - path to an image file
    parser.add_argument('--path', type=str, help='path to get images')

    # body - quote body to add to the image
    parser.add_argument('--body', type=str, help='body of text to be in meme')

    # author - quote author to add to the image
    parser.add_argument('--author', type=str, help='author of the text')

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))

from QuoteEngine.Ingestor import Ingestor
import os

quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
               './_data/DogQuotes/DogQuotesCSV.csv', './_data/DogQuotes/DogQuotesDOCX.docx',
               './_data/DogQuotes/DogQuotesIDK.idk',  './_data/DogQuotes/DogQuotesPDF.pdf']
print(quote_files)
for f in quote_files:
    try:
        Ingestor.parse(f)
    except ValueError as error:
        print(f"ValueError: {error}")

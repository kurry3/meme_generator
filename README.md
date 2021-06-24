# meme_generator

The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote.

Setting Up This Yourself

Install the packages listed in requirements.txt

Download and install the pdftotext tool: https://www.xpdfreader.com/download.html

Run the Application
The application can be run with the following command:
- python app.py
The application can be accessed at: https://localhost:5000

Sub-Modules
- QuoteEngine is a class that holds the body and author of a quote
- Ingestor encapsulates the helper classes below, calling the appropriate sub-module's parse function depending on the type of input file
Each of the sub-modules below realize the IngestorInterface which acts as a template for their functions
- CSVIngestor: uses the pandas library to create a list of QuoteModels from a csv file
- PDFIngestor: uses the pdftotext subprocess to create a list of QuoteModels from a pdf file
- DocxIngestor: uses the docx library to create a list of QuoteModels from a docx file
- TextIngestor: uses the built-in python libraries to create a list of QuoteModels from a txt file




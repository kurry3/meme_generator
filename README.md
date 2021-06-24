# meme_generator


The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote.

Setting Up This Yourself

1. Download this repository in a zipped folder and unzip it anywhere in your directory as you'd like. 
2. Open a command prompt/terminal in the root meme_generator-main folder (the name of the repository's zipped folder when the file was downloaded).
3. Run 'pip install -r requirements.txt' to install the libraries needed for the project.
4. Download and install the pdftotext tool: https://www.xpdfreader.com/download.html
To run this application via Python arg variables:
1. In the terminal, run 'python ./src/meme.py' with the optional commands of a string quote body, string quote author, and an image path.

To run this application on a web interface: 
1. In the terminal, run 'python ./src/app.py'
2. The application can be accessed at: https://localhost:5000

Sub-Modules
- QuoteEngine is a class that holds the body and author of a quote
- Ingestor encapsulates the helper classes below, calling the appropriate sub-module's parse function depending on the type of input file
Each of the sub-modules below realize the IngestorInterface which acts as a template for their functions
- CSVIngestor: uses the pandas library to create a list of QuoteModels from a csv file
- PDFIngestor: uses the pdftotext subprocess to create a list of QuoteModels from a pdf file
- DocxIngestor: uses the docx library to create a list of QuoteModels from a docx file
- TextIngestor: uses the built-in python libraries to create a list of QuoteModels from a txt file







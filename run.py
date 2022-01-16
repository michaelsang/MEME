
#from QuoteEngine import Ingestor, TextIngestor
#print(TextIngestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))


from QuoteEngine import Ingestor, DocxIngestor
print(DocxIngestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))

from pypdf import PdfReader

reader = PdfReader('./data/harrypotter_complete_edition.pdf')
print(len(reader.pages))
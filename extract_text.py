# Not used

from pypdf import PdfReader

# reader = PdfReader('./data/harrypotter_complete_edition.pdf')
reader = PdfReader('./data/HBP.pdf')
print(len(reader.pages))

# page = reader.pages[332]
# print(page.extract_text())

with open("./data/book.txt", 'w') as file:
    for page in reader.pages:
        file.write(page.extract_text() + "\n")
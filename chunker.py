import json
import os
import sys

book_path = './data/book.txt'

if not (os.path.isfile(book_path)):
    print("Txt file does not exist")
    sys.exit()

with open(book_path, 'r') as book_file:
    raw_book = book_file.read()
    book_chunks = raw_book.split('\n\n')

for chunk in book_chunks:
    print(chunk + "\n")

print(f'Number of chunks: {len(book_chunks)}')
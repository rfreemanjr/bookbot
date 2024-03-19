#This program should read files and then output them to a console
#@author Ronney Freeman

def main():
    file = "./books/frankenstein.txt"
    book = get_book(file)
    words = get_word_count(book)
    print(f"There are {words} words in this  document")

#This method will get the book
def get_book(book_path):
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

#This method will return the word count associated with the book.
def get_word_count(book):
    return len(book.split())

#Executes the main method of the program
main()

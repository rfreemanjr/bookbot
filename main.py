#This program should read files and then output them to a console
#@author Ronney Freeman

def main():
    file = "./books/frankenstein.txt"
    book = get_book(file)
    words = get_word_count(book)
    letters = get_letter_count(book)
    print(f"""
          --- Begin report of {file} ---
          There are {words} words in this document and the unique letter counts are as follows:\n
          """)
    get_letter_report(letters)
    print("--- End report ---")

#This method will get the book
def get_book(book_path):
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

#This method will return the word count associated with the book.
def get_word_count(book):
    return len(book.split())

#this method gets the letter count of each letter"
def get_letter_count(book):
    letter_dict = {
        'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,
        'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0
    }
    for letter in book:
        char = letter.lower()
        if char in letter_dict:
            letter_dict[char] += 1
    return letter_dict

def get_letter_report(dict):
    sorted_dict = sorted(dict)
    for i in range(0,len(dict)):
        print(f"The '{sorted_dict[i]}' character appears {dict[sorted_dict[i]]} times")
        

#Executes the main method of the program
main()

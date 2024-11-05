path = 'books/frankenstein.txt'

with open(path) as f:
    text = f.read()
    words = text.split()

    print(f"--- Begin report of {path} ---")
    print (f"{len(words)} words found in the document")
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # convert to object {letter: count}
    letter_count = {}
    
    for word in words:
        lowercase_words = word.lower()
        
        # return word count for each letter
        for letter in lowercase_words:
            if letter in alphabet:
                if letter not in letter_count:
                    letter_count[letter] = 1
                else:
                    letter_count[letter] += 1

    # loop through dict: The 'e' character was found 46043 times
    for letter, count in letter_count.items():
        print(f"The '{letter}' character was found {count} times")
    # print(letter_count)
    print("--- End report ---")



# how it was done in tutorial
# def main():
#   book_path = "books/frankenstein.txt"
#   text = get_book_text(book_path)
#   num_words = get_num_words(text)
#   chars_dict = get_chars_dict(text)
#   print(chars_dict)


# def get_num_words(text):
#     words = text.split()
#     return len(words)


# def get_chars_dict(text):
#     chars = {}
#     for c in text:
#         lowered = c.lower()
#         if lowered in chars:
#             chars[lowered] += 1
#         else:
#             chars[lowered] = 1
#     return chars


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()


# main()
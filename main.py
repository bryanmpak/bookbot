with open('books/frankenstein.txt') as f:
    text = f.read()
    words = text.split()
    
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


    print(letter_count)
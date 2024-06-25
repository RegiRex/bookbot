def main():
    book_path = 'books/frankenstein.txt'
    print(f"--- Begin report of {book_path} ---")
    text = get_text(book_path)
    words = count_words(text)
    chars = count_char(text)
    print(f"{words} words found in the text\n")
    for c in chars:
        print(f"The '{c}' character was found {chars[c]} times")
    print("--- End Report ---")

def get_text(path):
    with open('books/frankenstein.txt') as f:
        return f.read()

def count_words(text):
    word_count = len(text.split())
    '''for line in text:
        words = line.split()
        word_count += len(words)'''
    return word_count

def count_char(text):
    char_count = {}
    for line in text:
        lower_string = line.lower()
        for char in lower_string:
            if not char.isalpha():
                continue
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    char_count = dict(sorted(char_count.items()))
    return char_count

if __name__ == "__main__":
    main()
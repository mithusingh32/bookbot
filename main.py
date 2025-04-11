from stats import get_num_words, get_of_char_appear, get_sorted_dict_as_list
import sys

def get_book_text(file) -> str:
    book_content: str
    with open(file) as book:
        book_content = book.read()
    return book_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    
    book_path: str = sys.argv[1]
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    book = get_book_text(book_path)
    print('----------- Word Count ----------')
    print(f'{get_num_words(book)}')
    print('--------- Character Count -------')
    character = get_of_char_appear(book)
    char_list = get_sorted_dict_as_list(character)
    for char in char_list:
        if char['char'].isalpha():
            print(f'{char['char']}: {char['num']}')
    
main()

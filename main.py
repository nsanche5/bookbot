import sys
from stats import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = get_book_text(book_path)
    word_count = count_words(book)
    character_count = count_chars(book)
    sorted_list = dict_to_sort_list(character_count)

    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
        """)
    for dict in sorted_list:
        print(f"{dict["char"]}: {dict["count"]}")
    print("============= END ===============")

main()
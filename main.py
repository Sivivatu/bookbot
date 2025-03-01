from stats import get_num_words, get_book_text, unique_characters


def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    book_count = get_num_words(book_text)
    character_count = unique_characters(book_text)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{book_count} words found in the document")
    print("\n")
    for c in sorted(character_count, key=character_count.get, reverse=True):
        print(f"The character '{c}' was found {character_count[c]} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()

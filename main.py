import sys
from stats import word_counter, character_counter, sorted_dictionary


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():

    if len(sys.argv) == 2:

        input = sys.argv[1]
        word = word_counter(input)
        characters = character_counter(input)
        list_of_dictionaries = sorted_dictionary(input)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {input}...")
        print("----------- Word Count ----------")
        print(f"Found {word} total words")
        print("--------- Character Count -------")
        for character in list_of_dictionaries:
            if character["char"].isalpha() == False:
                continue
            else:
                ch = character["char"]
                num = character["num"]
                print(f"{ch}: {num}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
            
main()
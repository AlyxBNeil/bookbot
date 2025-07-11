import sys
from stats import get_num_words, get_num_characters, count_each_letter, char_report


print("sys.argv contains:", sys.argv)

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
        return text

def main():
    if len(sys.argv) != 2:
        # Print usage message and exit
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    counts = count_each_letter(text)
    report = char_report(counts)  # This creates the 'report' variable

    # Print formatted report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in report:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
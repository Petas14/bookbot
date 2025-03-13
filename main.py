from stats import get_num_words,get_cout_words
import stats
import sys
    
def main(book_path):
    
    
    # Count words and characters
    total_words, char_counts = stats.count_words_and_characters(book_path)
    
    # Get sorted character count
    sorted_counts = stats.sort_character_counts(char_counts)
    
    # Print formatted report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_counts:
        print(f"{item['character']}: {item['count']}")
    
    print("============= END ===============")
if __name__ == '__main__':
    if len(sys.argv) !=2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main(sys.argv[1])
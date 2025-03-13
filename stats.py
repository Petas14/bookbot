def get_num_words(path):
    with open(path, 'r') as f:
        return len(f.read().split())
    

def get_cout_words(path):
    with open(path, 'r') as f:
        text = f.read().lower()

    word_letter = {}
    for letter in text:
        if letter.isalpha():
            if letter in word_letter:
                word_letter[letter] += 1
            else:
                word_letter[letter] = 1
    return word_letter

def sort_character_counts(char_counts):
    """
    Takes a dictionary of characters and their counts, filters out non-alphabetical characters,
    and returns a sorted list of dictionaries from greatest to least by count.
    
    :param char_counts: dict, {char: count}
    :return: list of dictionaries, [{'character': char, 'count': count}, ...]
    """
    sorted_list = [
        {"character": char, "count": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]
    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    return sorted_list

def count_words_and_characters(filepath):
    """
    Reads a text file and counts words and characters.
    
    :param filepath: str, path to the text file
    :return: tuple (total word count, character count dictionary)
    """
    char_counts = {}
    total_words = 0

    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            total_words += len(words)

            for char in line.lower():  # Convert to lowercase for uniformity
                char_counts[char] = char_counts.get(char, 0) + 1

    return total_words, char_counts

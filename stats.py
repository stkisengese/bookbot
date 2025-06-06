
def count_words(words):
    content = words.split()
    return len(content)

def count_characters(text):
    char_counts = {}
    lower_text = text.lower()
    for char in lower_text:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_on_count(char_count):
    return char_count[1]

def print_report(word_count, char_counts):
    print("============ BOOKBOT ===========")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count -------------")
    print(f"Found {word_count} total words")
    print("--------- Character Count ----------")
    
    sorted_char = sorted(char_counts.items(), key=sort_on_count, reverse=True)

    for char, count in sorted_char:
        if char.isalpha():
            print(f"{char}: {count}")

    print("================ End ================")
    
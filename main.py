import string

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    generate_report(book_path, get_word_count(book_text), count_characters(book_text))


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def clean_character_dictionary(text):
    text = text.lower()

    # Remove punctuation using translation method
    translated_text = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translated_text)
    import code; code.interact(local=dict(globals(), **locals()))

    return clean_text

def count_characters(text):
    # Initialize dictionary for character counts
    char_count = {}
    # Create a dictionary of cleaned characters
    clean_text = clean_character_dictionary(text)
    
    # Count cleaned characters
    for clean_char in clean_text:
        if clean_char.isalpha():  # Check if the character is alphanumeric
            if clean_char in char_count:
                char_count[clean_char] += 1
            else:
                char_count[clean_char] = 1
    
    return char_count

def generate_report(book_path, word_count, char_count):
    # Print the report header
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    
    # Convert char_count dictionary to a list of dictionaries
    char_list = [{'char': char, 'count': count} for char, count in char_count.items()]
    
    # Sort char_list by count in descending order
    char_list.sort(key=lambda x: x['count'], reverse=True)
    
    # Print character counts
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    
    # Print the report footer
    print("--- End report ---")

# import code; code.interact(local=dict(globals(), **locals()))

main() 
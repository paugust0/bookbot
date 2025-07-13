import sys
from stats import get_word_count, get_char_count_dict, get_char_count_sorted_list

def get_text(file_path):
    with open(file_path) as file:
        return file.read()

def check_command_line_arguments(argument_list):
    if len(argument_list) == 2:
        file_path = argument_list[1]
        return file_path
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def show_char_counts(char_count_sorted_list):
    for char_count_pair in char_count_sorted_list:
        if char_count_pair["char"].isalpha():
            print(f"{char_count_pair["char"]}: {char_count_pair["count"]}")

def show_book_report(file_path):
    text = get_text(file_path)
    char_count_dict = get_char_count_dict(text)
    char_count_sorted_list = get_char_count_sorted_list(char_count_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(text)} total words")
    print("--------- Character Count -------")
    show_char_counts(char_count_sorted_list)
    print("============= END ===============")
    sys.exit(0)

def main():
    command_line_arguments = sys.argv
    file_path = check_command_line_arguments(command_line_arguments)
    show_book_report(file_path)

main()

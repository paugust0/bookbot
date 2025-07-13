def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count_dict(text):
    char_count_dict = {}
    for i in range(0, len(text)):
        char = text[i].lower()
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def sort_by_count(char_dict):
    return char_dict["count"]

def get_char_count_sorted_list(char_count_dict):
    char_count_sorted_list = []
    for char in char_count_dict:
        char_count_sorted_list.append({"char":char, "count":char_count_dict[char]})
    char_count_sorted_list.sort(reverse=True, key=sort_by_count)
    return char_count_sorted_list

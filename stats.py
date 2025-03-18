def get_book_text(filepath):
    text = ""
    with open(filepath) as f:
        text = f.read()
    return text

def count_words(text):
    words = text.split()
    count = len(words)
    return count

def count_chars(text):
    char_dict = {}
    for char in text:
        lower = char.lower()
        if lower in char_dict:
            char_dict[lower] += 1
        else:
            char_dict[lower] = 1
    return char_dict

def dict_to_sort_list(dict):
    sort_list = []
    for char in dict:
        if char.isalpha():
            sort_list.append({
                "char" : char,
                "count" : dict[char]
            })
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list
    
def sort_on(dict):
    return dict["count"]

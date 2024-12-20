def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return(file_contents)
        

def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        number_of_words = len(words)
        return(number_of_words)
    

def count_chars(f):
    character_count = {}
    lowered_chars = f.lower()
    for i in lowered_chars:
        if i in character_count:
            character_count[i] += 1
        else:
            character_count[i] = 1 
    return(character_count)


def char_count_text(f):
    for char in f:
        print(f"The '{char['character']}' character was found {char['count']} times")


def report():
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words} words found in the document")
    print()
    char_count_text(sort_on(count_chars(file_content)))
    print("--- End report ---")


def sort_on(dict):
    charlist = []
    for i in dict:
        if i.isalpha():
            char = {"character": i, "count": dict[i]}
            charlist.append(char)
    
    charlist.sort(key=lambda item: item["count"], reverse=True)
    return(charlist)

    
file_content = main()
num_of_words = count_words()
report()

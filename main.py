def main():
    global file_contents
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)

def word_count():
    global words
    words = file_contents.split()
    #print(f"There are {len(words)} words.")

def count_characters():
    global characters
    lower_contents = file_contents.lower()
    char = list(lower_contents)
    characters = {}
    for key in char:
        if key in characters:
            characters[key] += 1
        else:
            characters[key] = 1
    #print(characters)

def report():
    print(f"--- Begin report of books/frankenstein.txt ---\n{len(words)} words found in the document\n")
    character_list = []
    for key in characters:
        if key.isalpha():
            dictionary = {}
            dictionary["name"] = key
            dictionary["num"] = characters[key]
            character_list.append(dictionary)
    
    character_list.sort(reverse=True, key=lambda x: x["num"])
    for key in character_list:
        print(f"The '{key['name']}' character was found {key['num']} times")

main()
word_count()
count_characters()
report()
def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = file_contents.split()
    words_number = len(words)
    print(f"{words_number} words found in the document")

    character_ct = character_count(file_contents)
    character_list = []
    for char, count in character_ct.items():
        character_list.append({'char': char, 'num': count})

    def sort_on(character_list):
        return character_list["num"]
    character_list.sort(reverse=True, key=sort_on)

    for character in character_list:
        print(f"The '{character['char']}' character was found {character['num']} times")
    print("--- End report ---")


def character_count(file_contents):
    lowered = file_contents.lower()
    character_dict = {}
    for char in lowered:
        if char.isalpha() == True:
            if char in character_dict:
                character_dict[char] +=1
            else:
                character_dict[char] = 1
    return character_dict

    
main()

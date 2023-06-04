def switch_case(string):
    new_string = ""
    for letter in string:
        if letter.islower():
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    return new_string

print(switch_case(input("word: ")))


def aardvark(string):
    if string[0] == "a":
        return "aardvark"
    else:
        return "zebra"
        
word = input("write a word: ")

print(aardvark(word))

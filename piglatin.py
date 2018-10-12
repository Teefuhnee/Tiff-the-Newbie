pig = "ay"
word = raw_input("Enter word: ")

if (len(word) != 0 and word.isalpha()):
    print word
    first = word.lower()[0]
    print word[1:len(word)] + first + pig #starts displaying @ index 1

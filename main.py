# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.lower()
    anagram = anagram.lower()

    # the word/phrase are sorted in alphabetical order
    sorted_word = sorted(word)
    sorted_anagram = sorted(anagram)
    
    # empty lists are created, that will later be used to store only letters
    word_list = []
    anagram_list = []

    for word in sorted_word:
        if 'a' <= word <= 'z':
            word_list.append(word)
    print(word_list)

    for word in sorted_anagram:
        if 'a' <= word <= 'z':
            anagram_list.append(word)
    print(anagram_list)

    return word_list == anagram_list

    #print(sorted_word)
    #print(sorted_anagram)

print(find_anagram("Church of Scientology",  "rich-chosen goofy cult"))
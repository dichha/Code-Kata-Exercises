from collections import defaultdict
wordlist = []
#defaultdict takes comma in key not so in {} dict
anagram_dict = defaultdict(list)

def load_words(filename='word_list.txt'):
    with open(filename) as f:
        for word in f: 
            wordlist.append(word.rstrip())
    return wordlist

def making_dict(source):
    d = defaultdict(list)
    for word in source: 
        key = "".join(sorted(word))
        d[key].append(word)
    return d

def get_anagrams(word_source):
    d = making_dict(word_source)
    for key, anagrams in d.items():
        if len(anagrams) > 1:
            anagram_dict[key].append(anagrams)
    return anagram_dict

word_source = load_words()
anagrams = get_anagrams(word_source)


highest_anagram_wordlist = 0
highest_anagramlist = ""
longest_anagram_wordcount = 0
anagram_word_key = ""
for key, wordlist in anagrams.items():
    count = 0
    if(len(key) > longest_anagram_wordcount):
        longest_anagram_wordcount= len(key)
        anagram_word_key = key

    for word in wordlist:        
        for val in word:
            count += 1
    if (count > highest_anagram_wordlist):
        highest_anagramlist = wordlist
        highest_anagram_wordlist = count
        


word = ""        
anagram_list = anagrams[anagram_word_key]
for wordlist in anagram_list:
    word = ",".join(wordlist)  

print("Longest anagram key is: " + anagram_word_key +" and the value are "+ word +".") 
h_anagram = ""
h_anagramlist = highest_anagramlist
for wordlist in h_anagramlist:
    h_anagram = ",".join(wordlist)
print("Highest anagram list is: [" + h_anagram + "] which has " + str(highest_anagram_wordlist) + " words.")

    
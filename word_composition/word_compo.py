from timeit import default_timer as timer
def load_words(filename = '../anagram/word_list.txt'):
    wordforest = []
    with open(filename) as f:
        for word in f:          
            if len(word) < 8:
                word  = word.lower().strip()
                wordforest.append(word)
    return wordforest

def composed_words(wordforest):
    composed = []
    for word in wordforest:
        if(len(word) == 6):
            for i in range(6):
                check_word = word
                if(check_word[0:i+1] in wordforest):
                    if(check_word[i+1:] in wordforest):
                        composed.append((check_word[0:i+1], check_word[i+1:], word))
    return composed

def display(composed_words):
    for word in composed_words:
        part1, part2, compo = word
        print(part1 + " + " + part2 + " = " + compo)    
    



start = timer()                    
wordforest = load_words()
composed_words = composed_words(wordforest)
end = timer()
print("Time taken to find composite words: " + str(end-start))#328.2438080457365s ~ 5.47min
display(composed_words)

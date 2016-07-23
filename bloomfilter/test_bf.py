import math
import random 

from bloom_filter import BloomFilter
def bit_array_size(num_of_items,probability):
    bit_size = -(num_of_items * math.log(probability))/(math.log(2))**2
    return math.ceil(bit_size)

def size_of_hash(num_of_items, bit_array_size):
    hash_size = -(bit_array_size/num_of_items)* math.log(2)
    return abs(math.ceil(hash_size))
    
    
f = open('word_list.txt', 'r')
count=0
for line in f:
    count+=1
f.close()
    
num_of_items= count
print("Number of Items: " + str(num_of_items))
p = 0.005
print("Probability of false positive error " + str(p))


bit_size = bit_array_size(num_of_items, p)
print("Bit Size: "+str(bit_size))

hash_size = size_of_hash(num_of_items, bit_size)
print("Hash Size: "+str(hash_size))

bf = BloomFilter(num_of_items, hash_size)
word_list = open("word_list.txt").read().splitlines()

for word in word_list:
    bf.add(word)
word_list.close()
    
print(bf.lookup("99"))

print(bf.lookup("donkey")) 
print(bf.lookup("oitqv")) 
print(bf.lookup("fart"))
print(bf.lookup("Max"))
print(bf.lookup("Dichha"))
print(bf.lookup("Khuwalung"))

print("++++Random Word SpellChecker++++")


alpha=""
for i in range(97,123):
    alpha+=chr(i)
 
random_word=[] 
random_word_len=2000
for i in range(random_word_len):
    random_word.append(''.join(random.choice(alpha) for i in range(5)))
#print(random_word)
present=0
absent=0
ab_word=[]
for word in random_word:
    res = bf.lookup(word)
    if (res == "Probably"):
        present+=1
        #print(word)
    else:
        absent+=1
        ab_word.append(word)
print("Number of random words: " + str(random_word_len))
print("present word: " + str(present))
print("absent word: " + str(absent) + " which is "+str(((absent/random_word_len)*100))+"%")
print("Absent word list: " + str(ab_word))


        




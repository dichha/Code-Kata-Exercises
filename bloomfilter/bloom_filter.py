#bit_array = [0]*100
#print(bit_array)
##bit_array.setall(0)
#b1 = hash("apple1")#using 1 for seed
##taking out remainder
#index1 = b1%10
#bit_array[index1] = 1
class BloomFilter:        
    def __init__(self,size,hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0]*size
        
    def add(self, string):
        for seed in range(self.hash_count):
            seeded_word = string+str(seed)
            index = hash(seeded_word)%self.size
            #print(index)
            self.bit_array[index] = 1 
          
            
        
    def lookup(self, string):
        for seed in range(self.hash_count):
            seeded_word = string+str(seed)
            index = hash(seeded_word)%self.size
            if(self.bit_array[index] == 0):
                return "Nope"
        return "Probably"
        
    

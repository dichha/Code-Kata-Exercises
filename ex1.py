with open('weather.dat') as f:
    content = f.readlines()
last = len(content)
#print(last)
#print(content[2])
#print(content[last-2])
date = -1
smallest = 999
count = 0

for i in range(2,last-1):
    
    #print(content[i])
    #print(type(content[i]))
    values = (content[i].split(' '))
    val_list = [val for val in values if val != '']
    
    if(len(val_list[1]) == 2 and len(val_list[2]) == 2):
        
        diff = int(val_list[1])- int(val_list[2])
        count += 1
        
        if (diff < smallest):
            date =  val_list[0]
            #print("Date = " + str(date))
            smallest = diff
           
print("The day with smallest range of temperature difference is " + str(date)+"th day of the given month." ) 
#print(count)
f.close()
    
    
    
    

        
        

    
    


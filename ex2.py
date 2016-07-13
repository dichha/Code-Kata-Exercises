import math
with open('football.dat') as f:
    content = f.readlines()
#print(content)    
#print(len(content))
smallest = 999
team = ""
last = len(content)
for i in range(1,last):
    values = (content[i]).split(' ')
    val_list = [val for val in values if val != '']
    #print(val_list)
    if (len(val_list) > 1):
        for_goal = int(val_list[6])
        against_goal = int(val_list[8])
        diff = abs(for_goal - against_goal)
        
        if( diff < smallest):
            smallest = diff
            team = val_list[1]
            
print("The team with a smallest difference in goal for and against is " + team + " and the difference is " + str(smallest)+".")
f.close()

                            
        
        
               
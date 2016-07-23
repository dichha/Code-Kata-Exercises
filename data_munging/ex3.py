from refactor04 import *

print("========Football========")                  
with open('football.dat') as f:
    content = f.readlines()
end = len(content)
start = 1
smallest = 999
valueList = makeList(start, end, content)
ans = findSmallest(smallest, valueList, 6, 8, 1, "football")
print("The team with a smallest difference in goal for and against is " + ans + ".")
f.close()

print("========Weather========")        

with open('weather.dat') as f:
    content = f.readlines()
end = len(content)-1
start = 2
smallest = 999


valueList = makeList(start, end, content)
ans = findSmallest(smallest, valueList, 1, 2, 0, "weather")
print("The day with smallest range of temperature difference is " + str(ans)+"th day of the given month." ) 
f.close()

    
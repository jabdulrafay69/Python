set={1,2,3,4,"hello","world"}
print(set)
print(type(set))

 #methods
set.add(1) #adds a values into a set
set.add(2)
set.add(44)

set.remove(1)# removes a value from a set

set.clear() #removes all values from the set

set.add(1)
set.add(2)
set.add(44)


set.pop() #removes a random value


print(set)


set1={1,2,3}
set2={2,3,4}

#union and intersection between 2 sets
print(set1.union(set2))
print(set1.intersection(set2))

my_lists = [1,2,3]
my_list = [1,1.003,"Hello"]
len(my_list)
print(len(my_list))
print(my_list[0])
anotherlist=[4,5]
new_list = my_list + anotherlist

print(new_list)
new_list[0] = "ONE ALL CAPS"

print(new_list)
new_list.append("six")

print(new_list)
new_list.pop()
print(new_list)
popped_item = new_list.pop()
print(popped_item)

new_list.pop(1)
print(new_list)

t=(1,2,3)
mylist =[1,2,3]
myset=set()
myset.add(1)
myset.add(2)
myset.add(2)
print(myset)
myList=[1,1,1,1,2,2,2,2,2,3]
set(myList)

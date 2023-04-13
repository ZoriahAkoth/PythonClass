#list
numbers = [1,2,3,4,5,6,7,8,9,76]
names = ["zoria", "joy", "talia", "imela"]
counties = ["nairobi", "mombasa", "kisumu"]
print(names)
#adding new items/things to the list
names.append("betina")
print(names)
#index <from 0>
position1 = counties[0]
print(position1)
position3 = counties[2]
print(position3)

#add new item at specific position
fruits = ["pineapple", "apple", "kiwi", "orange"]
print(fruits)
fruits.insert(1,"watermelon")
fruits.insert(3, "blueberries")
print(fruits)

#to remove an item
fruits.pop()
print(fruits)
fruits.pop(2)
print(fruits)
fruits.remove("pineapple")
print(fruits)





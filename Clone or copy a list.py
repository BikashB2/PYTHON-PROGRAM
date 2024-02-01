myList = []
length = int(input("Enter number of elements : "))
for i in range(0, length):
    value = int(input())
    myList.append(value) 
copyList = myList.copy()

print("Entered List ", myList)
print("Cloned List ", copyList)
# Write a function to calculate the length of a number list and sum of list

inputList = input("Input a number list....")
numList = list(map(int,inputList.split()))
print(f"Entered list is : {numList}")

def lengthOfList(x):
    return len(x)

def sumOfList(x):
    return sum(x)

print(f"Length of the List is : {lengthOfList(numList)}")
print(f"Sum of the List is : {sumOfList(numList)}")

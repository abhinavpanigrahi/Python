inputNum = int(input("Enter a number for which you want to calculate the factorial.."))

def calcFatorial(num):
    fact = 1
    for i in range(1,num+1):
            fact *= i
          #  print(f"Inside if loop {fact}")
            i+=1
    return fact

factorial = calcFatorial(inputNum)
print(f"Factorial number of {inputNum} is {factorial}")
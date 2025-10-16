#function definition
def calcSum(num1,num2):
    sum = num1+num2
    return sum

print("Enter two numbers")
inputNum1 = float(input("Input first number..."))
inputNum2 = float(input("Input second number..."))

TotSum = calcSum (inputNum1,inputNum2)
print(f'Total sum of the two numbers is {TotSum}')
def fizz_buzz(input_number):
    for i in range(1, input_number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
                print("Fizz")
        elif i % 5 == 0:
                print("Buzz")
        else:
                print(i)

num = int(input("Enter a number: "))
fizz_buzz(num)
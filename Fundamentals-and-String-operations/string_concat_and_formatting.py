first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
name = first_name + " " + last_name
print("-----"*8)
print(f"Your full name is {name}")
print("-----"*8)
print("Your first name is: " + first_name +"\nYour last name is: " + last_name)
print("-----"*8)

salary = input("Enter your salary: ")
hike = input("Enter your hike in %: ")
new_salary = int(salary) + (int(salary) * int(hike)/100)
print(f"Your new salary after the hike is {new_salary}")
print("-----"*8)

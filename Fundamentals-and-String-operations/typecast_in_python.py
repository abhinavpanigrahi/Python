instructor_name = "Abhinav Panigrahi"
course_fees = "800"
course_rating = "4.8"
is_starting_soon = "True"
total_income = "None"

print("***** Before type casting *****")

print(type(instructor_name))
print(type(course_fees))
print(type(course_rating))
print(type(is_starting_soon))
print(type(total_income))


print("***** After type casting values *****")
print(str(instructor_name))
print(int(course_fees))
print(float(course_rating))
print(bool(is_starting_soon))
print(total_income)

print("***** After type casting *****")
print(type(str(instructor_name)))
print(type(int(course_fees)))
print(type(float(course_rating)))
print(type(bool(is_starting_soon)))
#print(None(total_income))
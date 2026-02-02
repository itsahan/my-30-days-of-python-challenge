# Day 2: 30 Days of python programming

first_name = 'its'
last_name = 'ahan'
full_name = first_name + ' ' + last_name
country = 'Small Country in Another World'
city = "Small City"
age = 250
is_married = False
is_true = True
is_light_on = False
print(first_name, last_name, country, city, age, is_married, is_true, is_light_on)

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))
if len(last_name) > len(first_name):
    print("last name is longer than first name")
elif len(first_name) < len(last_name):
    print("first name is shorter than last name")
else:
    print("first name and last name are of equal length")

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius
print("Area of circle:", area_of_circle)
print("Circumference of circle:", circum_of_circle)

print("\n--- User Information ---")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Country: {country}")
print(f"Age: {age}")

help('keywords')
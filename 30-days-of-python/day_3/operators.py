# Day 3: 30 Days of python programming

age = 2000
heigth = 1.79
x = 1 + 17j 

tri_base = 10
tri_height = 5
tri_area = 0.5 * tri_base * tri_height
print("The area of the triangle is:", tri_area)

tri_s_a = 7
tri_s_b = 4
tri_s_c = 2
tri_perimeter = tri_s_a + tri_s_b + tri_s_c
print("The perimeter of the triangle is:", tri_perimeter)

rect_length = 7
rect_width = 5
rect_area = rect_length * rect_width
rect_perimeter = 2 * (rect_length + rect_width)
print("The area of the rectangle is:", rect_area)
print("The perimeter of the rectangle is:", rect_perimeter)

cir_radius = 7
pi = 3.14
cir_area = pi * cir_radius ** 2
cir_circumference = 2 * pi * cir_radius
print("The area of the circle is:", cir_area)
print("The circumference of the circle is:", cir_circumference)

m = 2
b = -2

slope_8 = m
y_intercept = b
x_intercept = -b / m

print("The slope is:", slope_8)
print("The y-intercept is:", y_intercept)
print("The x-intercept is:", x_intercept)

x1 = 2
x2 = 6
y1 = 2
y2 = 10
slope_9 = (y2 - y1) / (x2 - x1)
pyhtagoras = ((x2 - x1) ** 2 + (y2 - y1) ** 2 ) ** 0.5
print("The slope between the points (2,2) and (6,10) is:", slope_9)
print ("The distance between the points (2,2) and (6,10) is:", pyhtagoras)

check = slope_8 == slope_9
print("Are the two slopes equal?", check)

s_list = [1, 0, -1, -2, -3, -4]
for s in s_list:
    y_s = s**2 + 6*s + 9
    print(f"When s = {s}, y = {y_s}")

py = 'python'
dr = 'dragon'
len_py = len(py)
len_dr = len(dr)
print("python" is "dragon")
print("on" in "python" and "on" in "dragon")
print('jargon' in "I hope this course is not full of jargon")
print("on" not in "python" and "on" not in "dragon")

fl_py = float(len_py)
str_py = str(fl_py)
print(py)
print(len_py)
print(fl_py)
print(str_py)

x = 7
if x % 2 == 0:
    print(f"{x} is an even number")
else:
    print(f"{x} is an odd number")

print(7 // 3 == int(2.7))

print(type('10') == type(10))

print(int(float('9.8')) == 10)

hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
weekly_earnings = hours * rate_per_hour
print(f"Your weekly earning is {weekly_earnings}")

year = int(input('Enter your age: '))
print(f"You have lived for {year * 31536000} seconds.")

for i in range(1, 6):
    print(i, i**0, i**1, i**2, i**3)

# Day 8: 30 Days of python programming

dog = {}
dog.update({'Name' : 'Bahlil',
            'Color' : 'Black', 
            'Breed' : 'Xoloitzcuintli', 
            'Age' : 49 
            })
print('Species details :', dog)

# first_name, last_name, gender, age, marital status, skills, country, city and address 
student = {
    'first_name': 'Joko',
    'last_name': 'Widodo',
    'gender': 'Male',
    'marital_status': True,
    'skills': ['Manipulation', 'Debt', 'Corruption'],
    'country': 'Indonesia',
    'Address': 'Solo'
    }
print('Student(?) :', student)

len_stud = len(student)
print('Student Lenght :', len_stud)

print(type(student['skills']))

student['skills'].extend(['Term-limit evasion', 'Immortality']) 
# use .extend([]) for more arguments, use .append() for only 1 argument
print(student)

keys = student.keys()
values = student.values()
print('Keys :', keys, '\nValues :', values)

items = student.items()
print('List of items :', items)

del student['skills']
print('skills' in student)

del student
try:
    print(student)
except NameError:
    print('He is gone for good')

# Day 8 Done!
# Day 9: 30 Days of python programming

'''
user = int(input('Enter your age: '))
if user >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18 - user} more years to learn to drive')
'''

'''
my_age = 20
your_age = int(input('Enter your age: '))
if your_age > my_age:
    print(f'You are {your_age - my_age} years older, than me.')
elif your_age < my_age:
    print(f'You need {my_age - your_age} more years to face me.')
else:
    print('I see, you have become stronger, but not enough to stand on my side.')
'''

'''
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b:
    print(f'{a} is greater than {b}.')
elif a < b:
    print(f'{a} is smaller than {b}.')
else:
    print(f'{a} is equal to {b}.')
'''

'''
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
'''

'''
try:
    score = int(input('Input score: '))
    
    if 90 <= score <= 100:
        print('Grade A')
    elif 80 <= score <= 89:
        print('Grade B')
    elif 70 <= score <= 79:
        print('Grade C')
    elif 60 <= score <= 69:
        print('Grade D')
    elif 0 <= score <= 59:
        print('Grade F')
    else:
        print('Invalid score')

except ValueError:
    print('Please input numbers only')
'''

'''
autumn = ['september', 'october', 'november']
winter = ['december', 'january', 'february']
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']

month = input('Please enter the month: ').lower()
if month in autumn:
    print('Winter is coming.')
elif month in winter:
    print('Winter is here.')
    respond = input('Respond: ')
    if respond == "Well, father always promised, didn't he?":
        print('You are goat.')
    else:
        print('I am sorry, never mind. It is Winter by the way.')
elif month in spring:
    print(' It is Spring')
elif month in summer:
    print('It is Summer')
else:
    print('Please use Gregorian Calendar.')
'''

'''
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits_input = input('Enter the fruit: ').lower()
if fruits_input in fruits:
    print('That fruit already exists in the list')
else:
    fruits.append(fruits_input)
    print(fruits)
'''

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
        }

if 'skills' in person:
    skills = person['skills']
    print(f'This person can do {skills[len(skills)//2]}')
else:
    print('This person does not have any skills')

if 'skills' in person:
    if 'Python' in person['skills']:
        print(f"And {person['skills'][-1]}")
else:
    print('else')

skills = person['skills']

if skills == ['JavaScript', 'React']:
    print('He is a front end developer')

elif ('Node' in skills and 
      'Python' in skills and 
      'MongoDB' in skills):
    print('He is a backend developer')

elif ('React' in skills and 
      'Node' in skills and 
      'MongoDB' in skills):
    print('He is a fullstack developer') #idk how to get here yet, maybe next time.

else:
    print('unknown title')

if person['is_married'] and person['country'] == 'Finland':
    full_name = person['first_name'] + ' ' + person['last_name']
    print(f'{full_name} lives in {person["country"]}. He is married')
else:
    print()

# Done.
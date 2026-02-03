# Day 4: 30 Days of python programming

"""
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")

%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision

"""
aa = 'Thirty'
ab = 'Days'
ac = 'Of'
ad = 'Python'
formatted_string = "%s %s %s %s" % (aa, ab, ac, ad)
print(formatted_string)

ae = 'Coding'
af = 'For'
ag = 'All'
formatted_string2 = "{} {} {}".format(ae, af, ag)
print(formatted_string2)

company = "Coding For All"
print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[0:6])
#or 
print(company.split()[0])

print(company.index("Coding"))
#or
print("Coding" in company)
#or
print(company.find("Coding"))

company.replace('Coding', 'Python')
print(company)

company1 = "Python for Everyone"
print(company1.replace('Everyone', 'All'))

print(company.split())

no12 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(no12.split(','))

print(company[0]) #first character

print(company[-1]) #last character

print(company[10]) #character at index 10

print("".join([word[0] for word in company1.split()])) #Accronym or abbreviation

print("".join([word[0] for word in company.split()])) #Accronym or abbreviation

print(company.index('C')) #index of character C in the string

print(company.index('F')) #index of character F in the string

print(company.rfind('l')) #last index of character l in the string

sentence = 'You cannot end a sentence with because because because is a conjunction'
fs_sentence = sentence.find('because') #first index of the word because in the string
print(fs_sentence)

ls_sentence = (sentence.rindex('because')) #last index of the word because in the string
print(ls_sentence)

last_index = ls_sentence + len('because')
print(last_index)

print(sentence[fs_sentence:last_index]) #slicing out the word 'because' in the string

print(company.startswith('Coding'))

print(company.endswith('Coding'))

company2 = "   Coding For All      "
print(company2.strip()) # removes the spaces
print(company2)

identifier1 = '30DaysOfPython'
identifier2 = 'thirty_days_of_python'
print(identifier1.isidentifier())
print(identifier2.isidentifier())

list1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(list1))

print('I am enjoying this challenge.\nI just wonder what is next.')

'''
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
'''

print('Name\t  Age\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

'''
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
'''

radiusc = 10
areac = 3.14 * radiusc ** 2
print(f"The area of a circle with radius {radiusc} is {int(areac)} meters square.")

num8 = 8
num6 = 6
print(f'{num8} + {num6} = {num8 + num6}')
print(f'{num8} - {num6} = {num8 - num6}')
print(f'{num8} * {num6} = {num8 * num6}')
print(f'{num8} / {num6} = {num8 / num6:.2f}') # add :.2f to format to 2 decimal places
print(f'{num8} % {num6} = {num8 % num6}')
print(f'{num8} // {num6} = {num8 // num6}')
print(f'{num8} ** {num6} = {num8 ** num6}')

# Done
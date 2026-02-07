# Day 7: 30 Days of python programming

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

lenght1 = len(it_companies)
print('Lenght = ', lenght1)

it_companies.add('Twitter')
print(it_companies)

multi = ('Komdigi', 'Coretax', 'Telkomsel')
it_companies.update(multi)
print(it_companies)

it_companies.remove('Google')
print(it_companies)

'''
it_companies.remove('Tesla')
print(it_companies)

it_companies.discard('Tesla')
print(it_companies)

Removing item(s) that is not in the set using .remove will occur Error, but .discard is not.
'''

C = A | B
print(C)

intersc_AB = A.intersection(B)
print(intersc_AB)

subset_AB = A.issubset(B)
print(subset_AB)

disjoint_AB = A.isdisjoint(B)
print(disjoint_AB)

join_AB = A | B
join_BA = B | A
print(join_AB)
print(join_BA)

# I'm sorry, is this right? Because it has same results. The .union and .update as well.

symm_diff_AB = A.symmetric_difference(B)
print(symm_diff_AB)

del A
del B

age_ls = list(age)
print("Lenght List: ", len(age_ls))
print("Leght Set: ", len(age))

'''
String: All that in between either ' ' or  " "
List: Variable that have various items, changeable, ordered, and duplicable, [].
Tuple: Is a list, but unchangeable, ().
Set: Same as list, tuple could have items but onl those tha immuteable. Not duplicable, unordered and changeable, {}.
'''

sentence = 'I am a teacher and I love to inspire and teach people'
words = sentence.split()
print(words)
set_words = set(words)
print('Total uniqe words: ', len(set_words))
print(set_words)

# Done, 7/7!!
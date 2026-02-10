# Day 10: 30 Days of python programming

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(f'The example count ends here {count}')

num_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in num_1:
    print(number)

num_1_2 = 0
while num_1_2 < 11:
    print(num_1_2)
    num_1_2 += 1
else:
    print('No. 1 Done')

num_1.sort(reverse=True)
for number in num_1:
    print(number)

num_2 = 11
while num_2 == 0:
    print(num_2)
    num_2 -= 1
else:
    print('No. 2 Done')

num_3 = '#'
while len(num_3) <= 7:
    print(num_3)
    num_3 += '#'
else:
    print('No. 3 Done') 

for num_4_line in range(8):
    for num_4_coloumn in range(8):
        print('#', end=' ')
    print()
else:
    print('No. 4 Done')

num_5 = 0
while num_5 * num_5 <= 100:
    times_5 = num_5 * num_5
    print(f'{num_5} x {num_5} = {times_5}')
    num_5 += 1
else:
    print('No. 5 Done')

num_6 = ['Python', 'Numpy','Pandas','Django', 'Flask']
for num_6_lst in num_6:
    print(num_6_lst)
else:
    print('No. 6 done')

num_7 = 0
while num_7 <= 100:
    if num_7 %2 == 0:
        print(num_7)
        if num_7 == 100:
            break
    num_7 += 1
else:
    print('something is wrong')
'''
bruh, the chatgpt suggest me a shorter code

for num in range(0, 101, 2):
    print(num)
'''

for num_8 in range(1, 101, 2):
    print(num_8) # or just the reverse version code above

sum_2_1 = 0
for num_2_1 in range(0, 101):
    sum_2_1 += num_2_1
print(sum_2_1)
'''
bruh, i ask chatgpt and he give me one line code

print(sum(range(0, 101)))
'''

sum_2_even = 0
for num_2_even in range(0, 101, 2):
    sum_2_even += num_2_even
print(sum_2_even)

sum_2_odd = 0
for num_2_odd in range(1, 101, 2):
    sum_2_odd += num_2_odd
print(sum_2_odd)

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_folder import countries # I literaly spends half an hour to look for how to import this mf data instead of copas it.

for land in countries.countries:
    if 'land' in land:
        print(land)

fruits = ['banana', 'orange', 'mango', 'lemon']
for fruitss in range(len(fruits) -1, -1, -1):
    print(fruits[fruitss])

'''
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
'''

from data_folder.countries_data import countries_data

languages = []

for country in countries_data:
    for lang in country["languages"]:
        if lang not in languages:
            languages.append(lang)

print(len(languages))

lang_count = {}
for country in countries_data:
    for lang in country["languages"]:
        if lang in lang_count:
            lang_count[lang] += 1
        else:
            lang_count[lang] = 1

sorted_langs = []
for lang in lang_count:
    sorted_langs.append((lang, lang_count[lang]))

for i in range(len(sorted_langs)):
    for j in range(i+1, len(sorted_langs)):
        if sorted_langs[i][1] < sorted_langs[j][1]:
            sorted_langs[i], sorted_langs[j] = sorted_langs[j], sorted_langs[i]

print("Top 10:", sorted_langs[:10])

top_10_countries = []  

for country in countries_data:
    name = country["name"]
    pop = country["population"]
    
    top_10_countries.append((name, pop))
    
    for i in range(len(top_10_countries)):
        for j in range(i+1, len(top_10_countries)):
            if top_10_countries[i][1] < top_10_countries[j][1]:
                top_10_countries[i], top_10_countries[j] = top_10_countries[j], top_10_countries[i]
    
    top_10_countries = top_10_countries[:10]

print("Top 10 populated:")
for name, pop in top_10_countries:
    print(f"{name}: {pop:,}")

# Day 5: 30 Days of python programming

'''
There are four collection data types in Python :

List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
'''

empty_list = []
print(empty_list)

zionist = ['Netanyahu', 'Trump', 'Biden', 'Prabowo', '02 Voters']
print(zionist)

print(len(zionist))

print(f"{zionist[0]}, {zionist[len(zionist)//2]}, {zionist[-1]}")

mixed_data_types = ["itsahan", 2000, 186, "Not Married", "Earth"]
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

print(len(it_companies))

print(f"{it_companies[0]}, {it_companies[len(it_companies)//2]}, {it_companies[-1]}")
#or
print(it_companies[::3])

it_companies[-1] = 'Teh Sosro'
print(it_companies)

it_companies.append('Coretax')
print(it_companies)

it_companies.insert(len(it_companies)//2, 'Indosat Ooredoo')
print(it_companies)

it_companies[-1] = it_companies[-1].upper()
print(it_companies)

print('#;  '.join(it_companies))

print('CORETAX' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[:3])

print(it_companies[-3:])

middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    print(it_companies[middle_index - 1: middle_index + 1])
else:
    print(it_companies[middle_index])

it_companies.pop(0)
print(it_companies)

middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    del it_companies[middle_index - 1: middle_index + 1]
else:
    it_companies.pop(middle_index)
print(it_companies)

it_companies.pop(-1)
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies
# print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

front_end2 = front_end.copy()
full_stack = front_end2.insert(len(front_end2)//2 + 1, 'Python')
full_stack = front_end2.insert(len(front_end2)//2 + 2, 'SQL')
print(front_end2)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(ages)
print(f"Min age: {min_age}\nMax age: {max_age}")

ages.append(min_age)
ages.append(max_age)
ages.sort()
print(ages)

x = len(ages)
if x % 2 == 0:
    median = (ages[x//2 - 1] + ages[x//2]) / 2  
    print(f"Median: {median}")
else:
    median = ages[x//2]
    print(f"Median: {median}")

avg = sum(ages) / x
print(f"Average: {avg}")

age_range = max_age - min_age
print(f"Range: {age_range}")

x1 = abs(min_age - avg)
x2 = abs(max_age - avg)
print(f"Distance between min and average: {x1}\nDistance between max and average: {x2}")

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
countries.sort()
mid_con = len(countries) // 2
if len(countries) % 2 == 0:
    print(countries[mid_con - 1], countries[mid_con])
else:
    print(countries[mid_con])

first_half = countries[:len(countries)//2 + 1]
second_half = countries[len(countries)//2 + 1:]
print(f"First_half: {first_half}")
print(f"Second_half: {second_half}")
print(len(first_half))
print(len(second_half))

whatever_im_tired = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
one_con, two_con, three_con, *rest = whatever_im_tired
print(f"First Country: {one_con}")
print(f"Second Country: {two_con}")
print(f"Third Country: {three_con}")
print(f"Scandiac Countries: {rest}")

# Done T-T, kinda late, sorry for that to my future self.
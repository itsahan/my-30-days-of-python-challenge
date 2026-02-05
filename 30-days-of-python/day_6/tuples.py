# Day 6: 30 Days of python programming

empty_tuple = ()
print("Empty Tuple:", empty_tuple)

bro = ('Stewie', 'Bart')
sister = ('Meg', 'Lisa')
siblings = bro + sister
print("Siblings Tuple:", siblings)

print("Number of Siblings:", len(siblings))

family_members = list(siblings)
family_members.append('Peter')
family_members.append('Lois')
print("Family Members List:", family_members)

siblings, parents = family_members[0:4], family_members[4:]
print("Siblings:", siblings)
print("Parents:", parents)

fruits = ('durian', 'orange', 'apple')
veggies = ('carrot', 'chilli', 'potato')
meat = ('chicken', 'beef', 'egg')
food_stuff_tp = fruits + veggies + meat
print("Food Stuff Tuple:", food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print("Food Stuff List:", food_stuff_lt)

food_stuff_lt.sort()
print("Sorted Food Stuff List:", food_stuff_lt)
mid_lt = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    print("Middle Two Items:", food_stuff_lt[mid_lt - 1: mid_lt + 1])
else:
    print("Middle Item:", food_stuff_lt[mid_lt])

fs_3 = food_stuff_lt[:3]
ls_3 = food_stuff_lt[-3:]
print("First Three Items:", fs_3)
print("Last Three Items:", ls_3)

del food_stuff_tp
try:
    'apple' in food_stuff_tp
except NameError:
    print("food_stuff_tp has been deleted")

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

'Estonia' in nordic_countries

'Iceland' in nordic_countries

# Done, it's quite straightforward and quicker than lists!
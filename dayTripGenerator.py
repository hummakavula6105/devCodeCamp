from difflib import restore
from random import random
from secrets import choice


destinations_list = ['Park','Zoo','Childrens Museum','Pool']
restaurants_list = ['Cheddards','Vegan Turnip','Smokey Bones','Mi Tequila']
transportation_list = ['Car', 'Train', 'Boat', 'Horse & Buggy']
entertainment_list = ['Movie', 'Games', 'Swimming', 'Croquet']
greeting = ('Welcome to the day trip generator! We help you choose what you do for the day, so you won\'t have to!')
selection_greeting = ('Please look over the destination, restaurant, transportation, & entertainment for your day.')

import random
# print(random.choice(destinations_list))
# print(choice(destinations_list))

# print(choice(restaurants_list))

# print(choice(transportation_list))

# print(choice(entertainment_list))

destination = random.choice(destinations_list)
restaurant = random.choice(restaurants_list)
transportation = random.choice(transportation_list)
entertainment = random.choice(entertainment_list)

print(greeting + ' ' + selection_greeting)
print(f' {destination} {restaurant} {transportation} {entertainment}')






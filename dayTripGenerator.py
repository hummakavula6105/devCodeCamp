import random

destinations_list = ['Park','Zoo','Childrens Museum','Pool']
restaurants_list = ['Cheddards','Vegan Turnip','Smokey Bones','Mi Tequila']
transportation_list = ['Car', 'Train', 'Boat', 'Horse & Buggy']
entertainment_list = ['Movie', 'Games', 'Swimming', 'Croquet']
greeting = ('Welcome to the day trip generator! We help you choose what you do for the day, so you won\'t have to!')
selection_greeting = ('Please look over the destination, restaurant, transportation, & entertainment for your day.')


destination = random.choice(destinations_list)
restaurant = random.choice(restaurants_list)
transportation = random.choice(transportation_list)
entertainment = random.choice(entertainment_list)


print(greeting + ' ' + selection_greeting)
print(f'Your destination will be {destination}\nYour restaurant will be {restaurant}\nYour form of transportation will be {transportation}\nYour entertainment will be {entertainment}\n.')


user_choice = input('Do you want to make changes? ')

while user_choice == 'Y':

    user_choice = input('''Please select from the following:
                1. Destination
                2. Restaurant
                3. Transportation
                4. Entertainment
                5. ALL
                ''')
    if user_choice == 1:
        destination = random.choice(destinations_list)
    elif user_choice == 2:
        restaurant = random.choice(restaurants_list)
    elif user_choice == 3:
        transportation = random.choice(transportation_list)
    elif user_choice == 4:
        entertainment = random.choice(entertainment_list)
    else:
        destination = random.choice(destinations_list)
        restaurant = random.choice(restaurants_list)
        transportation = random.choice(transportation_list)
        entertainment = random.choice(entertainment_list)


print('Enjoy your day and thank you for choosing our Day Trip Generator!')





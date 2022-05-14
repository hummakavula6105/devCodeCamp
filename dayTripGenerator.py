import random


destinations_list = ['Park','Zoo','Childrens Museum','Pool']
restaurants_list = ['Cheddards','Vegan Turnip','Smokey Bones','Mi Tequila']
transportation_list = ['Car', 'Train', 'Boat', 'Horse & Buggy']
entertainment_list = ['Movie', 'Games', 'Swimming', 'Croquet']
greeting = ('Welcome to the day trip generator! We help you choose what you do for the day, so you won\'t have to!')
selection_greeting = ('Please look over the destination, restaurant, transportation, & entertainment for your day.')

def get_destination():
    destination = random.choice(destinations_list)
    return destination
def get_restaurant():
    restaurant = random.choice(restaurants_list)
    return restaurant
def get_transportation():
    transportation = random.choice(transportation_list)
    return transportation
def get_entertainment():
    entertainment = random.choice(entertainment_list)
    return entertainment

destination = get_destination()
restaurant = get_restaurant()
transportation = get_transportation()
entertainment = get_entertainment()


print(greeting + ' ' + selection_greeting)
print(f'Your destination will be {destination}.\nYour restaurant will be {restaurant}.\nYour form of transportation will be {transportation}.\nYour entertainment will be {entertainment}.\n')


user_choice = input('Do you want to make changes?   Y/N \n')             

while user_choice[0].upper() == 'Y':

    decisions = input('''\nPlease select from the following:
                1. Destination
                2. Restaurant
                3. Transportation
                4. Entertainment
                5. ALL
                \n''')
    if decisions == str(1):
        destination = get_destination()
    elif decisions == str(2):
        restaurant = get_restaurant()
    elif decisions == str(3):
        transportation = get_transportation()
    elif decisions == str(4):
        entertainment = get_entertainment()
    else:
        destination = get_destination()
        restaurant = get_restaurant()
        transportation = get_transportation()
        entertainment = get_entertainment()
        
        
    print(f'\nYour destination will be {destination}.\nYour restaurant will be {restaurant}.\nYour form of transportation will be {transportation}.\nYour entertainment will be {entertainment}.\n')
    user_choice = input('Do you wish to make any additional changes?   Y/N \n')


print('Enjoy your day and thank you for choosing our Day Trip Generator!')






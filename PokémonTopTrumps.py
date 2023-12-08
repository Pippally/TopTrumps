#1. Generate a random number between 1 and 151 to use as the Pokemon ID
#Using the Pokemon API get a Pokemon based on its ID number
#Create a dictionary that contains the returned Pokemon's name, id, height and weight
#Get a random Pokemon for the player and another for their opponent
#5. Ask the user which stat they want to use (id, height or weight)
#6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins


import random, requests

print("""
┌───────────────────────────────────────────────────────────────────────────────┐
│ __                         __                                                 │
│/\ \__                     /\ \__                                              │
│\ \ ,_\   ___   _____      \ \ ,_\  _ __   __  __    ___ ___   _____     ____  │
│ \ \ \/  / __`\/\ '__`\     \ \ \/ /\`'__\/\ \/\ \ /' __` __`\/\ '__`\  /',__\ │
│  \ \ \_/\ \L\ \ \ \L\ \     \ \ \_\ \ \/ \ \ \_\ \/\ \/\ \/\ \ \ \L\ \/\__, `\│
│   \ \__\ \____/\ \ ,__/      \ \__\  \_\  \ \____/\ \_\ \_\ \_\ \ ,__/\/\____/│
│    \/__/\/___/  \ \ \/        \/__/ \/_/   \/___/  \/_/\/_/\/_/\ \ \/  \/___/ │
│                  \ \_\                                          \ \_\         │
│                   \/_/                                           \/_/         │
└───────────────────────────────────────────────────────────────────────────────┘""")

def random_pokemon():
    pokemon_number = random.randint(1,151)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }

my_pokemon = random_pokemon()
print(f"You have been given {my_pokemon['name']}")
print(f"Your stats are...")
print(f"""    
            ** id number: - {my_pokemon['id']} **
            ** height: - {my_pokemon['height']} **
            ** weight: - {my_pokemon['weight']} ** 

""")

def check_input(user_input, correct_options):
    return user_input in correct_options

# Define the list of correct options
correct_options = ["height", "id", "weight"]

while True:
    user_input = input('Which stat do you want to use? (id, height, weight) :- ')

    # Check if the input is correct
    if check_input(user_input, correct_options):
        print(" ")
        print("Now let's compare... good luck!.")
        print(" ")
        break  # Exit the loop if the input is correct
    else:
        print("Oops! You entered the wrong input. Please try again.")
        print(" ")


opponent_pokemon = random_pokemon()
print(f"The opponent chose {opponent_pokemon['name']}")
print(f"The opponent stats are...")
print(f"""    
            ** id number: - {opponent_pokemon['id']} **
            ** height: - {opponent_pokemon['height']} **
            ** weight: - {opponent_pokemon['weight']} ** 

""")

my_stat = my_pokemon[user_input]
opponent_stat = opponent_pokemon[user_input]

if my_stat > opponent_stat:
    print('Your stat is higher. You Win!')
elif my_stat < opponent_stat:
    print('Your stat is lower. You Lose!')
else:
    print('Your stat matches your opponents, Draw game!')





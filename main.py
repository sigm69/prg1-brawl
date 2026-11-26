import random
import time


def stamina_drain(stamina_drain,stamina):
    stamina = stamina_drain-stamina

# Startvärdena väljer du själv.

running = True

game_stats = {
    "player1": {
        "hp": 100,
        "armour": 100,
        "stamina": 100,
    },
    "fiende1": {
        "name": "Kirk",
        "hp": 50,
        "armour": 25,
        "stamina": 50,
        "skada": 5,
    },
    "fiende2": {
        "name": "Jens.First phase",
        "hp": 100,
        "armour": 25,
        "stamina": 100,
        "skada": 15,
    },
    "fiende3": {
        "name": "david",
        "hp": 200,
        "armour": 25,
        "stamina": 200,
        "skada": 20,
    },
    "fiende4": {
        "name": "Tiger 2",
        "hp": 500,
        "armour": 100,
        "stamina": 1,
        "skada": 100,
    },
    "fiende5": {
        "name": "mbt",
        "hp": 10000,
        "armour": 250,
        "stamina": 1,
        "skada": 250,
    },
    "fiende6": {
        "name": "Jens. last phase",
        "hp": 25000,
        "armour": 500,
        "stamina": 1,
        "skada": 1000,
    },
}
weapons_list = [
    {
        "name": "rocket launcher",
        "damage": (250, 500),
        "block": 0,
    },
    {
        "name": "katana",
        "damage": (5, 200),
        "block": 15,
    },
    {
        "name": "laser beam",
        "damage": (10000, 100000),
        "block": 100,
    },
    {
        "name": "stick",
        "damage": (1000, 1000),
        "block": 0,
    },
    {
        "name": "water gun",
        "damage": (0, 100),
        "block": 5,
    },
]


# Ditt första kort börjar här.

gamename = ("Gladiator battle")
print("-"*20)
print (gamename)
player_1 = input("player name...")

print("""\nweapons\nrocketlauncher\nkatana\nlaser beam\nstick\nwater gun\n""")

chosen_weapon = None

while chosen_weapon == None:
    Choice = input ("type a weapon name").lower()
    for weapon in weapons_list:
        if weapon["name"] == Choice:
            chosen_weapon = weapon
            break
        else:
            print("weapon not found ")


if chosen_weapon:
    print(f"You chose: {chosen_weapon['name']}")
else:
    print("Weapon not found!\n")



print("""\narmour\nHeavy armour\nLight armour\nmedium armour\n""")

while True:
    armour = input(f"{player_1} choose armour...").lower()
    if armour == ("light armour") or armour == ("light"):
        player1_armour = 0
        player1_stamina_drain = 0
        print(f"{player_1} armour {player1_armour} stamina drain {player1_stamina_drain}")
        break
    elif armour == ("medium armour") or armour == ("medium"):
        player1_armour = 25
        player1_stamina_drain = 25
        print(f"{player_1} armour {player1_armour} stamina drain {player1_stamina_drain}")
        break
    elif armour == ("heavy armour") or armour == ("heavy"):
        player1_armour = 50
        player1_stamina_drain = 50
        print(f"{player_1} armour {player1_armour} stamina drain {player1_stamina_drain}")
        break
    else:
        print("you typed incorectly try again")

print("\nPress enter to start")
input()
print (game_stats["fiende1"])



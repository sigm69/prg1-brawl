import random
import time


# Startvärdena väljer du själv.

game_stats = {
    "player1": {
        "hp": 100,
        "armour": 100,
        "stamina": 100,
    },
    "fiende1": {
        "hp": 50,
        "armour": 25,
        "stamina": 50,
        "skada": random.randint(1, 5),
    },
    "fiende2": {
        "hp": 100,
        "armour": 25,
        "stamina": 100,
        "skada": random.randint(1, 15),
    },
    "fiende3": {
        "hp": 200,
        "armour": 25,
        "stamina": 200,
        "skada": random.randint(5, 20),
    },
    "tiger2": {
        "hp": 500,
        "armour": 100,
        "stamina": 1,
        "skada": random.randint(25, 100),
    },
    "tank": {
        "hp": 10000,
        "armour": 250,
        "stamina": 1,
        "skada": random.randint(50, 250),
    },
    "boss": {
        "hp": 25000,
        "armour": 500,
        "stamina": 1,
        "skada": random.randint(1, 1000),
    },
}

# Ditt första kort börjar här.

gamename = ("Gladiator battle")
print("-"*20)
print (gamename)
player_1 = input("player name...")

print("""\nweapons\nrocketlauncher (5 shoots)\nkatana\nlaser beam (one time use)\nstick\nwater gun\n""")

while True:
    weapon = input(f"{player_1} choose weapon...").lower()
    if  weapon == ("rocketlauncher"):
        player1_damage = 25
        player1_block_power = 0
        print("damage 25 "+"block 0")
        break
    elif weapon == ("katana"):
        player1_damage = random.randint(5,20)
        player1_block_power = 15
        print("damage 5-20 "+"block 15")
        break
    elif weapon == ("laser beam"):
        player1_damage = 10000
        player1_block_power = 100
        print("damage 10000 "+ "block 100")
        break
    elif weapon == ("stick"):
        player1_damage = random.randint(-100,100)
        player1_block_power = 0
        print("damage -100-100 "+"block 0")
        break
    elif weapon == ("water gun"):
        player1_damage = random.randint(0,10)
        player1_block_power = random.randint(1,5)
        print("damage 0-10 "+"block 1-5")
        break
    else:
        print("you typed incorectly try again")

print("""\narmour\nHeavy armour\nLight armour\nmedium armour""")

while True:
    armour = input(f"{player_1} choose armour...").lower()
    if armour == ("light armour"):
        player1_armour = 0
        player1_stamina_drain = 0
        print(f"{player_1} armour {player1_armour} stamina drain {player1_stamina_drain}")
        break
    elif armour == ("medium armour"):
        player1_armour = 25
        player1_stamina_drain = 25
        print(f"{player_1} armour {player1_armour} stamina drain {player1_stamina_drain}")
        break
    elif armour == ("heavy"):
        player1_armour = 50
        player1_stamina_drain = 50
        print(f"{player_1} armour {player1_armour} stamina drain {player1_stamina_drain}")
        break
    else:
        print("you typed incorectly try again")

print("Press enter to start")
input()
print(game_stats)
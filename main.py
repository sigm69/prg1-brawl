import random
import time

def liv_kvar(player1_damage, fiende_armour):
    print (player1_damage / fiende_armour)


# Startvärdena väljer du själv.

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
        "skada": random.randint(1, 5),
    },
    "fiende2": {
        "name": "Jens.First phase",
        "hp": 100,
        "armour": 25,
        "stamina": 100,
        "skada": random.randint(1, 15),
    },
    "fiende3": {
        "name": "david",
        "hp": 200,
        "armour": 25,
        "stamina": 200,
        "skada": random.randint(5, 20),
    },
    "fiende4": {
        "name": "Tiger 2",
        "hp": 500,
        "armour": 100,
        "stamina": 1,
        "skada": random.randint(25, 100),
    },
    "fiende5": {
        "name": "mbt",
        "hp": 10000,
        "armour": 250,
        "stamina": 1,
        "skada": random.randint(50, 250),
    },
    "fiende6": {
        "name": "Jens. last phase",
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

player1_turn = input("Attack or Block ").lower
if player1_turn == "attack":
    liv_kvar(player1_damage, 25)
    
    
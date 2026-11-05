import random

# Startvärdena väljer du själv.

Player1_liv = 100
fiende_num_1_hp = 100
fiende_num_2_hp = 150
fiende_num_3_hp = 200
tiger_fiende_num_4_hp = 500
tank_fiende_num_5_hp = 10000

fiende1_skada = random.randint(1,5)
fiende2_skada = random.randint(1,15)
fiende3_skada = random.randint(5,20)
fiende4_skada = random.randint(5,30)
fiende5_skada = random.randint(50,250)

# Ditt första kort börjar här.

gamename = ("Gladiator battle")
print("-"*20)
print (gamename)
player_1 = input("name-")

print("""\nrocketlauncher (5 shoots)\nkatana\nlaser beam (one time use)\nstick\nwater gun\n""")
weapon = input(f"{player_1} choose weapon...").lower()
while True:
    if  weapon == ("rocketlauncher"):
        player1_damage = 25
        player1_block_power = 0
        print("damage 25"+"block 0")
        break
    elif weapon == ("katana"):
        player1_damage = random.randint(5,20)
        player1_block_power = 15
        print("damage 5-20"+"block 15")
        break
    elif weapon == ("laser beam"):
        player1_damage = 10000
        player1_block_power = 100
        print("damage 10000"+ "block 100")
        break
    elif weapon == ("stick"):
        player1_damage = random.randint(-100,100)
        player1_block_power = 0
        print("damage -100-100"+"block 0")
        break
    elif weapon == ("water gun"):
        player1_damage = random.randint(0,10)
        player1_block_power = random.randint(1,5)
        print("damage 0-10"+"block 1-5")
    else:
        print("you typed incorectly try again")

print
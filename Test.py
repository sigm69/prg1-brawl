import random
def Fighting_turn(player1_hp, weapon_damage, weapon_block, fiende_armour, fiende_hp, fiende_skada, player1_stamina, player1_staminadrain):
    global running
    global turn
    while turn:
        attack_or_block = input("\nType attack to attack \nAnd block to block \n ").lower()
        weapon_damage = random.randint(25,500)
        weapon_block = 10
        if player1_stamina >0:
            if attack_or_block == "attack" or attack_or_block == "a":
                sigma = weapon_damage / fiende_armour
                fiende_hp = fiende_hp-sigma
                Liv_kvar = fiende_skada
                player1_hp = player1_hp-Liv_kvar
                player1_stamina = player1_stamina - player1_staminadrain
                print(f"\ndin skada {sigma}")
                print(f"fiendens liv {fiende_hp}")
                print(f"ditt liv {player1_hp}")
                print(f"stamina kvar {player1_stamina}")
            elif attack_or_block == "block" or attack_or_block == "b":
                Liv_kvar = fiende_skada/weapon_block
                player1_hp = player1_hp-Liv_kvar
                player1_stamina = player1_stamina + 25
                print(f"ditt liv {player1_hp}")
                print(f"fiendens liv {fiende_hp}")
                print(f"din stamina {player1_stamina}")
            else:
                print("")
            if fiende_hp <= 0:
                running = False
                turn = False
                print ("\ndu vann grattis")
            elif player1_hp <=0:
                print("\ndu dog starta om")
                running = False
                turn = False
            else:
                running = True
                turn = True
        else:
            player1_stamina = player1_stamina + 50
            player1_hp = player1_hp-fiende_skada
            print(f"\ndin stamina tog slut \ndin nuvarande stamina är {player1_stamina}")
            print(f"ditt liv{player1_hp}")
            print(f"fiendens liv {fiende_hp}")


weapons_list ={
    "rocket launcher":{
        "damage": 250-500,
        "block": 0,
    },
    "katana":{
        "damage": 5-200,
        "block": 15,
    },
    "laser beam":{
        "damage": 10000-100000,
        "block": 100,
    },
    "stick":{
        "damage": 1000-1000,
        "block": 0,
    },
    "water gun":{
        "damage": 0-100,
        "block": 5,
    }
}

running = True
turn = True

while running:
    weapon_damage = random.randint(25,500)
    weapon_block = 10
    player1_hp = 100
    print("fight 1")
    Fighting_turn(player1_hp, weapon_damage,weapon_block, 25, 50, 5, 100, 25)
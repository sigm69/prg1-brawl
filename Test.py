import random
def Fighting_turn1232424242(player1_hp, weapon_damage, weapon_block, fiende_armour, fiende_hp, fiende_skada, player1_stamina, player1_staminadrain):
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



def Fighting_turn(player1_hp, weapon_min, weapon_max, weapon_block, fiende_armour, fiende_hp, fiende_skada, player1_stamina, player1_staminadrain):
    global running
    global turn
    döda_datorn = 10
    while turn:
        attack_or_block = input("\nType attack to attack \nAnd block to block \n ").lower()
        weapon_damage = random.randint(weapon_min,weapon_max)
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
                time.sleep(15)
                while True:
                    döda_datorn = döda_datorn *99999
                    print(döda_datorn)
                    if döda_datorn == 1:
                        break
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
def power_up_pickup(player1_hp, weapon_min, weapon_max, player1_stamina, player1_staminadrain, player1_armour):
    more_hp = player1_hp + 25
    more_stamina = player1_stamina
    better_armoure = player1_armour
    less_stamina_drain = player1_staminadrain
    more_attack_power = weapon_max *0.25 + weapon_max and weapon_min *0.25 + weapon_min
    print(more_hp or more_stamina or better_armoure or less_stamina_drain or more_attack_power)


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

Fighting_turn(25, 5, 500, 5, 10, 1, 1, 100, 0)
power_up_pickup(25, 5, 500, 100, 25, 10)
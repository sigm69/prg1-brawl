import random
def Fighting_turn(player1_hp, weapon_damage, weapon_block, fiende_armour, fiende_hp, fiende_skada, player1_stamina, player1_staminadrain):
    global running
    global turn
    while turn:
        attack_or_block = input("\nType attack to attack \n Type block to block \n If you do not type attack or block i will assume you to block \n").lower()
        weapon_damage = random.randint(25,500)
        weapon_block = 10
        if player1_stamina <=0:
            if attack_or_block == "attack":
                sigma = weapon_damage / fiende_armour
                fiende_hp = fiende_hp-sigma
                Liv_kvar = fiende_skada
                player1_hp = player1_hp-Liv_kvar
                player1_stamina = player1_stamina - player1_staminadrain
                print(f"\ndin skada {sigma}")
                print(f"fiendens liv {fiende_hp}")
                print(f"ditt liv {player1_hp}")
                print(f"stamina kvar {player1_stamina}")
            elif attack_or_block == "block":
                Liv_kvar = fiende_skada/weapon_block
                player1_hp = player1_hp-Liv_kvar
                print(player1_hp)
            else:
                Liv_kvar = fiende_skada/weapon_block
                player1_hp = player1_hp-Liv_kvar
                print(f"ditt liv{player1_hp}")
            if fiende_hp <= 0:
                running = False
                turn = False
                print ("du vann grattis")
            elif player1_hp <=0:
                print("du dog starta om")
                running = False
                turn = False
            else:
                running = True
                turn = True
        else:
            player1_stamina + 50
            Liv_kvar = fiende_skada/weapon_block
            player1_hp = player1_hp-Liv_kvar
            print(f"ditt liv{player1_hp}")


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
    Fighting_turn(player1_hp, weapon_damage,weapon_block, 25, 50, 45, 100, 25)
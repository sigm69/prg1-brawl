import random
def Fighting_runda(player1_hp, weapon_damage, weapon_block, fiende_armour,fiende_hp,fiende_skada):
    global running
    global turn
    while turn:
        attack_or_block = input("Type attack to attack \n Type block to block \n If you do not type attack or block i will assume you to block").lower()
        weapon_damage = random.randint(25,500)
        weapon_block = 10
        if attack_or_block == "attack":
            sigma = weapon_damage / fiende_armour
            fiende_hp = fiende_hp-sigma
            print(f"din skada {sigma}")
            print(f"fiendens liv{fiende_hp}")
            Liv_kvar = fiende_skada
            player1_hp_kvar = player1_hp-Liv_kvar
            print(player1_hp_kvar)
        elif attack_or_block == "block":
            Liv_kvar = weapon_block-fiende_skada
            player1_hp_kvar = player1_hp-Liv_kvar
            print(player1_hp_kvar)
        else:
            Liv_kvar = weapon_block-fiende_skada
            player1_hp_kvar = player1_hp-Liv_kvar
            print(player1_hp_kvar)
            if fiende_hp <= 0:
                running = False
                print ("du van grattis")
            elif player1_hp_kvar <=0:
                print("du dog starta om")
            else:
                running = True

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
    Fighting_runda(player1_hp, weapon_damage,weapon_block, 25, 50, 5)
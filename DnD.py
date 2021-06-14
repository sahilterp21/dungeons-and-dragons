import random

# Enemies defined in different dictionaries
vampire = {"name": "Vampire", "attack":"1d5", "defense": "1d3", "maxhp":50, "curhp":50 }
goblin = {"name": "Goblin", "attack":"1d3", "defense": "1d1", "maxhp":30, "curhp":30 }
ghost = {"name": "Ghost", "attack":"1d5", "defense": "1d5", "maxhp":50, "curhp":50 }
dracula = {"name": "Dracula", "attack":"2d5", "defense": "1d4", "maxhp":200, "curhp":200 }

# A LIST of DICTIONARIES for enemies
enemies = [vampire, goblin, ghost, dracula]

# Player dictionary
player = {"name":"", "attack":"2d5", "defense": "1d3", "maxhp":200, "curhp":200}

def get_roll(rollstring):
    splt = (rollstring.split('d'))
    a = int(splt[0])
    b = int(splt[1])
    c = 0
    for i in range(0,a):
        d = random.randint(0,b)
        c = c + d
    return c

def get_damage(attack, defense):
    attack_vec = get_roll(attack)
    defense_vec = get_roll(defense)
    if defense_vec > attack_vec:
        return 0
    else:
        return attack_vec - defense_vec

def do_battle(player, enemy):
    php = player["curhp"]
    ehp = enemy["curhp"]
    while True:
        playerAttack = get_damage(player["attack"],enemy["defense"])
        ehp = ehp - playerAttack

        if ehp <1:
            return True
        print(("{} does {} damage to {}").format(player["name"],playerAttack, enemy["name"]))
        print(("{} hp: ").format(player["name"]), php)
        print(("{} hp: ").format(enemy["name"]), ehp)
        #time.sleep(1) ##remove this
        enemyAttack = get_damage(enemy["attack"], player["defense"])
        php = php - enemyAttack
        player["curhp"] = php
        if php <1:
            return False
        print(("{} does {} damage to {}").format(enemy["name"], enemyAttack, player["name"]))
        print(("{} hp: ").format(player["name"]), php)
        print(("{} hp: ").format(enemy["name"]), ehp)


def main_menu_goto_battle():
    enemy = enemies[random.randint(0,len(enemies)-1)]
    if do_battle(player, enemy):
        print(f"The {enemy['name']} has died, hurray!")
        enemy['curhp'] = enemy['maxhp']
        input("Press enter to return home")
    else:
        print(f"Oh no! {player['name']}")

    return


def main_menu_heal():
    print(f"The player takes rest under a healing fountain. HP restored!")
    player['curhp'] = player['maxhp']
    input("Press enter to return home")
    return


def main_menu():
    # Player dies if player HP reaches 0 or less
    while player['curhp'] > 0:
        # Display menu
        print(f"{player['name']} currently has {player['curhp']} hp\n")
        print("1 : Go to Battle")
        print("2 : Heal")

        x = input("What to do next > ")
        # Get input from player
        if x =="1":
            main_menu_goto_battle()
        elif x=="2":
            main_menu_heal()
        else:
            print("No such action")

    print("Player is dead!")


player['name'] = input("What is the player's name? ")
main_menu()



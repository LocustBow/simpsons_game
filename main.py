import random
from collections.abc import Iterable

from characters import Character, BART, HOMER


def get_player(characters: Iterable[Character]) -> Character:
    while True:
        print("Choose a character.")
        for character in characters:
            print(f" * {character}")
        player_name = input(">>> ").title()
        player = next((character for character in characters if character.name == player_name), None)
        if player:
            return player

        print("Invalid choice.")


def get_computer(characters: Iterable[Character], player: Character) -> Character:
    available_options = [character for character in characters if character != player]
    return random.choice(available_options)


def start_battle(player: Character, computer: Character) -> None:
    # clear()
    print(f"{player.image}\n{player}\nHP: {player.hp}/{player.max_hp}")
    print("\nVERSUS\n")
    print(f"{computer.image}\n{computer}\nHP: {computer.hp}/{computer.max_hp}")


def attack(attacker: Character, defender: Character) -> None:
    # clear()
    defender_original_hp = defender.hp
    damage = attacker.attack(defender)
    print(f"{attacker} attacks!")
    print(attacker.attack_image)
    print(random.choice(attacker.attack_expressions))
    print(f"Damage: {damage}")
    print(defender.damage_image)
    print(random.choice(defender.damage_expressions))
    print(f"HP: {defender_original_hp} - {damage}")
    print(f"HP: {defender.hp}")


player = get_player([BART, HOMER])
computer = get_computer([BART, HOMER], player)

fighting = True
attacker, defender = player, computer

print("It's time for a battle.")
# clear()
start_battle(player, computer)
print("\nYOU get to attack first!\n")
input("Press any key to continue... ")

while fighting:
    attack(attacker, defender)

    input("Press any key to continue... ")
    # clear()

    if defender.hp <= 0:
        fighting = False
    else:
        attacker, defender = defender, attacker

print(f"{defender} was murdered!  {attacker} wins!")

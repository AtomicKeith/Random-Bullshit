from os import system

system("title Keith's Text-Based Adventure")
system('cls')

player_name = input("What is your name? > ")
player_race = input("What is your race? (Human, Elf, Dwarf, Orc) > ")

print("   ___ _                     _              ___              _   _          ")
print("  / __| |_  __ _ _ _ __ _ __| |_ ___ _ _   / __|_ _ ___ __ _| |_(_)___ _ _  ")
print(" | (__| ' \/ _` | '_/ _` / _|  _/ -_) '_| | (__| '_/ -_) _` |  _| / _ \ ' \ ")
print("  \___|_||_\__,_|_| \__,_\__|\__\___|_|    \___|_| \___\__,_|\__|_\___/_||_|")
print("                                                                            \n")

print(player_name)

if player_name != input("What is your name? > "):
    system('cls')

print("   ___ _                     _              ___              _   _          ")
print("  / __| |_  __ _ _ _ __ _ __| |_ ___ _ _   / __|_ _ ___ __ _| |_(_)___ _ _  ")
print(" | (__| ' \/ _` | '_/ _` / _|  _/ -_) '_| | (__| '_/ -_) _` |  _| / _ \ ' \ ")
print("  \___|_||_\__,_|_| \__,_\__|\__\___|_|    \___|_| \___\__,_|\__|_\___/_||_|")
print("                                                                            \n")

print(f"Name: {player_name}")

print (player_race)

system('cls')
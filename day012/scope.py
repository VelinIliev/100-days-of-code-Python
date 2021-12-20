enemies = 1

def increase_enemies():
    # global enemies
    # enemies = 2
    print(f'enemies inside function: {enemies}')
    return enemies + 1

enemies = increase_enemies()
print(f'enemies outside function: {enemies}')

# player_helth = 10

# potion_strength = 0

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_helth)

#     drink_potion()

# print(player_helth)

# game_level = 3
# enemies = ["Skeletons", "Zombie", "Alien"]
# if game_level < 5 :
#     new_enemy = enemies[0]

# print(new_enemy)
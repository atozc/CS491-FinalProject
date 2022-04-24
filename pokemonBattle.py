import Enemies 
from Enemies import damageDone, generatePokemon
import random

#allows the user to choose their starter pokemon
def chooseyourstarter():
    print("Choose your starter pokemon!")
    print("Enter 1 for Chimchar, the fiesty fire-type chimp!")
    print("Enter 2 for Piplup, the cool water-type penguin!")
    print("Enter 3 for Turtwig, the humble grass-type turtle!\n")
    choice = input("Enter the number of your choice: ")
    if choice == '1':
        print("\nYou chose Chimchar!")
        chimchar = {'name': 'Chimchar','HP': 44, 'Attack': 58, 'Defense': 44}
        return chimchar
    elif choice == '2':
        print("\nYou chose Piplup!")
        piplup = {'name': 'Piplup','HP': 53, 'Attack': 51, 'Defense': 53}
        return piplup
    else:
        print("\nYou chose Turtwig!")
        turtwig = {'name': 'Turtwig','HP': 55, 'Attack': 68, 'Defense': 64}
        return turtwig

#prints the basic introduction for the user
def introduction():
    print("Welcome! Test your skills in the Pokemon Marathon!")
    print("You will choose a pokemon and try to battle as many pokemon as you can before your pokemon faints!\n")

#tracks the pokemon's health and returns the starting HP
def isPokemonAlive(pokemon):
    HP = pokemon['HP']
    print(pokemon['name'])
    print('current health: ' + str(HP))
    return HP

#The pokemon Chimchar
def chimchar(enemy):
    enemyhealth = enemy['HP']
    enemydefense = enemy['Defense']
    power = 0.5
    #if user chose chimchar, it allows them to choose and use a move

    #returns the move
    moves = [('Ember', 40),('Flame Wheel', 60),('Fire Spin', 35),('Flamethrower',90)]
    print("Choose a move!")
    print("1 - Ember")
    print("2 - Flame Wheel") 
    print("3 - Fire Spin")
    print("4 - Flamethrower") 
    movechoice = input("Enter move choice: ")
    if movechoice == '1':
        print("Chimchar used Ember!")
        movepower = 40
        damage = movepower * power
    elif movechoice == '2':
        print("Chimchar used Flame Wheel!")
        movepower = 60
        damage = movepower * power
    elif movechoice == '3':
        print("Chimchar used Fire Spin!")
        movepower = 35
        damage = movepower * power
    else:
        print("Chimchar used Flamethrower!")
        movepower = 90
        damage = movepower * power
    defended = damage * (int(enemydefense) / 100)
    resultingHP = int(enemyhealth) - defended
    print(enemy['name'] + " lost " + str(defended) + " HP points!\n")
    return (resultingHP)

#Pokemon Piplulp
def piplup(enemy):
    enemyhealth = enemy['HP']
    enemydefense = enemy['Defense']
    power = 0.5
    '''if user chose piplup, it allows them to choose and use a move'''
    moves = [('Bubble',40),('Bubble Beam', 65),('Brine', 65),('Whirlpool', 35)]
    print("Choose a move!")
    print("1 - Bubble") 
    print("2 - Bubble Beam")
    print("3 - Brine")
    print("4 - Whirlpool")
    movechoice = input("Enter move choice: ")
    if movechoice == '1':
        print("Piplup used Bubble!")
        movepower = 40
        damage = movepower * power
    elif movechoice == '2':
        print("Piplup used Bubble Beam!")
        movepower = 65
        damage = movepower * power
    elif movechoice == '3':
        print("Piplup used Brine!")
        movepower = 65
        damage = movepower * power
    else:
        print("Piplup used Whirlpool!")
        movepower = 35
        damage = movepower * power
    defended = damage * (int(enemydefense) / 100)
    resultingHP = int(enemyhealth) - defended
    print(enemy['name'] + " lost " + str(defended) + " HP points!\n")
    return (resultingHP)

#Pokemon Turtwig
def turtwig(enemy):
    '''if user chose turtwig, it allows them to choose and use a move'''
    enemyhealth = enemy['HP']
    enemydefense = enemy['Defense']
    power = 0.5
    moves = [('Razor Leaf', 55),('Bite', 60),('Tackle', 40),('Crunch', 80)]
    print("Choose a move!")
    print("1 - Razor Leaf")
    print("2 - Bite")
    print("3 - Tackle")
    print("4 - Crunch")
    movechoice = input("Enter move choice: \n")
    if movechoice == '1':
        print("Turtwig used Razor Leaf!")
        movepower = 55
        damage = movepower * power
    elif movechoice == '2':
        print("Turtwig used Bite!")
        movepower = 60
        damage = movepower * power
    elif movechoice == '3':
        print("Turtwig used Tackle!")
        movepower = 40
        damage = movepower * power
    else:
        print("Turtwig used Crunch!")
        movepower = 80
        damage = movepower * power
    defended = damage * (int(enemydefense) / 100)
    resultingHP = int(enemyhealth) - defended
    print(enemy['name'] + " lost " + str(defended) + " HP points!\n")
    return (resultingHP)

#Move
def move(pokemon, enemy):
    '''activates certain moveset based on which pokemon is chosen'''
    if pokemon['name'] == 'Chimchar':
        return chimchar(enemy)
    elif pokemon['name'] == 'Piplup':
        return piplup(enemy)
    else:
        return turtwig(enemy)

#Runs game
def runGame():
    introduction()
    pokemon = chooseyourstarter()
    health = isPokemonAlive(pokemon)
    pokecount = 0
    while health > 0:
        enemy = Enemies.encounter()
        enemyhealth = int(enemy['HP'])
        pokecount += 1
        while enemyhealth > 0:
            enemyhealth = move(pokemon, enemy)
            if enemyhealth < 0:
                continue
            enemy['HP'] = enemyhealth
            health = damageDone(enemy, pokemon)
            pokemon['HP'] = health
            print(pokemon['name']+ " HP: " + str(pokemon['HP']))
            print(enemy['name']+ " HP: " + str(enemy['HP']) + "\n")
            if health < 0:
                print("Your " + pokemon['name'] + " fainted. :(\n")
                print("You encountered " + str(pokecount) + " pokemon.")
                break

runGame()
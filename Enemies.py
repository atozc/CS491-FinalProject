import random 

#Pokemon for random enemy generation
def generatePokemon():
    starly = {'name': 'Starly', 'HP': 40, 'Attack': 55, 'Defense':30}
    kricketot = {'name': 'Kricketot', 'HP': 37, 'Attack': 25, 'Defense':41}
    bidoof = {'name': 'Bidoof', 'HP': 59, 'Attack': 45, 'Defense':40}
    rattata = {'name': 'Rattata', 'HP': 30, 'Attack': 56, 'Defense':35}
    meowth = {'name': 'Meowth', 'HP': 40, 'Attack': 45, 'Defense': 35}
    skitty = {'name': 'Skitty', 'HP': 50, 'Attack': 45, 'Defense': 45}
    pokemon = [starly, kricketot, bidoof, rattata, meowth, skitty]
    chooseenemy = random.choice(pokemon)
    return chooseenemy

#Starts encounter
def encounter():
    enemy = generatePokemon()
    print("\nYou encountered a " + enemy['name'] + "!")
    return(enemy)

#Enemy makes move and damage is calculated 
def damageDone(enemy, pokemon):
    moveset = [('Pound', 40),('Quick Attack', 40), ('Scratch', 40), ('Swift',60)]
    choice = random.choice(moveset)
    move = choice[0]
    print(enemy['name'] + " used " + move + "!")
    power = int(enemy['Attack']) / 100
    movepower = int(choice[1])
    damage = movepower * power
    '''calculates defended amount of attack'''
    defended = damage * (int(pokemon['Defense']) / 100)
    resultingHP = int(pokemon['HP']) - defended
    print(pokemon['name'] + " lost " + str(defended) + " HP points!")
    return (resultingHP)


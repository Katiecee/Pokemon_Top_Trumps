import random  # Imports random module into the game.
import requests  # Imports requests module into the game.
from time import sleep  # Imports time module into the game.


def playagain():    # Prompt user to play again.
    input("Play again? Press any key to continue: - ")


def pokecard():  # Pulls data from PokeAPI.
    card = random.randint(1, 151)
    url = f"https://pokeapi.co/api/v2/pokemon/{card}"
    response = requests.get(url)
    data = response.json()
    return {
        'name': data['name'].capitalize(),
        'id': data['id'],
        'height': data['height'],
        'weight': data['weight'],
        'abilities': [ability["ability"]["name"] for ability in data["abilities"]],
        'types': [type_data["type"]["name"] for type_data in data["types"]],
        'hp': data["stats"][0]["base_stat"],
        'attack': data["stats"][1]["base_stat"],
        'defense': data["stats"][2]["base_stat"],
    }


def restartgame(): # Starts game again if user input error.
    player = pokecard()
    sleep(1)
    print("OK, " + playername + ", let's try again!")
    startgame()


def startgame():  # Player selects card, and program relays stats to player.
    player = pokecard()
    input("To begin, select a card from the deck by pressing any key, then Enter: - ")
    print("You got {}!".format(player['name']), )
    type1 = player['types']
    print("Their type is {}.".format(type1[0]))
    sigmove1 = random.choice(player['abilities'])
    print("{}'s signature move is {}.".format(player['name'], sigmove1))
    sleep(1)
    print("Their height is {}.".format(player['height']), )
    sleep(1)
    print("Their weight is {}.".format(player['weight']), )
    sleep(1)
    print("Their HP is {}.".format(player['hp']), )
    sleep(1)
    print("Their attack is {}.".format(player['attack']), )
    sleep(1)
    print("Their defense is {}.".format(player['defense']), )
    sleep(1)

    def continuegame():  # Chooses computer card and compares statistics.
        print("What stat would you like to use?")
        while True:
            choice = input("Pick from height, weight, HP, attack or defense - ").lower()
            choicelist = ["height", "weight", "hp", "attack", "defense"]
            if choice in choicelist:
                print("You have selected... {}!".format(choice), )
                computer = pokecard()
                print('The computer chooses {}!'.format(computer['name']))
                sleep(1)
                type2 = computer['types']
                print("Their type is {}.".format(type2[0]))
                sigmove1 = random.choice(computer['abilities'])
                print("{}'s signature move is {}.".format(computer['name'], sigmove1))
                sleep(1)
                print("Their height is {}.".format(computer['height']), )
                sleep(1)
                print("Their weight is {}.".format(computer['weight']), )
                sleep(1)
                print("Their HP is {}.".format(computer['hp']), )
                sleep(1)
                print("Their attack is {}.".format(computer['attack']), )
                sleep(1)
                print("Their defense is {}.".format(computer['defense']), )
                sleep(1)
                playerstat = player[choice]
                computerstat = computer[choice]
                if playerstat > computerstat:
                    print("{} demolishes {} in battle!".format(player['name'], computer['name']), )
                    sleep(1)
                    print("Congratulations, " + playername + "! You are the winner!")
                    sleep(1)
                    playagain()
                    startgame()
                elif playerstat < computerstat:
                    print("{} demolishes {} in battle!".format(computer['name'], player['name']), )
                    sleep(1)
                    print("Sorry, " + playername + "! You lose!")
                    sleep(1)
                    playagain()
                    startgame()
                else:
                    print('Both {}'.format(player['name']), " and {}".format(computer['name']),
                          ' are locked in battle...')
                    sleep(1)
                    print("It's a draw, no one wins this time!")
                    sleep(1)
                    playagain()
                    startgame()
            else:
                print("I'm sorry,  I didn't understand. Please try again.")
                print("What stat would you like to use?")
    while True:
        restart = input("Would you like to use this card? Y to continue, N to restart. - ").upper()
        if restart == "Y":
            continuegame()
        elif restart == "N":
            restartgame()
        else:
            print("Sorry, I don't understand! Answer must be Y or N.")

# Inputs player name.
print("Hi! Welcome to Pokemon Top Trumps. To begin, please enter your name.")
playername = input("Your name here: - ").capitalize()
print("Thank you, " + playername + "!")
startgame()
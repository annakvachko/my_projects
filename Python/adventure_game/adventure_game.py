import time
import random


def print_pause(text):
    print(text)
    time.sleep(2)


def intro_message(character):
    print_pause('You find yourself standing in an open field, filled with '
                'grass and yellow wildflowers.')
    print_pause(f'Rumor has it that a {character} is somewhere around here, '
                'and has been terrifying the nearby village.')
    print_pause('In front of you is a house.')
    print_pause('To your right is a dark cave.')
    print_pause('In your hand you hold your trusty (but not very effective)'
                ' dagger.')


def decision_numerical():
    choice = input('(Please enter 1 or 2.)\n')
    if choice == '1':
        return choice
    elif choice == '2':
        return choice
    else:
        decision_numerical()


def decision_string():
    choice = input('Please enter y (yes) or n (no)\n')
    if choice == 'y':
        return choice
    elif choice == 'n':
        return choice
    else:
        decision_string()


def play_again():
    print_pause('Would you like to play again? (y/n)')
    choice = decision_string()
    if choice == 'y':
        adventure_game()
    else:
        print_pause('Thanks for playing! See you next time.')


def where_to_go(character, item, weapon):
    print_pause('Enter 1 to knock on the door of the house.')
    print_pause('Enter 2 to peer into the cave.')
    print_pause('What would you like to do?')
    choice = decision_numerical()
    if choice == '1':
        house(character, item, weapon)
    else:
        cave(character, item, weapon)


def cave_goodbye():
    print_pause('You walk back out to the field.')


def cave(character, item, weapon):
    print_pause('You peer cautiously into the cave.')
    print_pause('It turns out to be only a very small cave.')
    if weapon == item:
        print_pause('You\'ve been here before, and gotten all the good '
                    'stuff. It\'s just an empty cave now.')
        cave_goodbye()
        where_to_go(character, item, weapon)
    else:
        print_pause('Your eye catches a glint of metal behind a rock.')
        print_pause(f'You have found the {weapon}')
        print_pause(f'Do you want to exchange your dagger for the {weapon}')
        choice = decision_string()
        if choice == 'y':
            item = weapon
            print_pause('You discard your silly old dagger and take '
                        f'the {weapon} with you.')
            cave_goodbye()
            where_to_go(character, item, weapon)
        else:
            cave_goodbye()
            where_to_go(character, item, weapon)


def battle(character, item, weapon):
    print_pause('Would you like to (1) fight or (2) run away?')
    choice = decision_numerical()
    if choice == '1':
        if item == weapon:
            print_pause(f'The {item} shines brightly in your hand as you'
                        ' brace yourself for the attack.')
            print_pause(f'But the {character} takes one look at your shiny'
                        ' new toy and runs away!')
            print_pause(f'You have rid the town of the {character}. You'
                        ' are victorious!')
            play_again()
        else:
            print_pause('You do your best...')
            print_pause(f'but your dagger is no match for the {character}.')
            print_pause('You have been defeated!')
            play_again()
    else:
        print_pause('You run back into the field. Luckily, you don\'t '
                    'seem to have been followed.')
        where_to_go(character, item, weapon)


def house(character, item, weapon):
    print_pause('You approach the door of the house.')
    print_pause('You are about to knock when the door opens and '
                f'out steps a {character}.')
    print_pause(f'Eep! This is the {character}\'s house!')
    print_pause(f'The {character} attacks you!')
    battle(character, item, weapon)


def adventure_game():
    characters = ['thursty demon', 'wicked witch', 'elf-alcoholic',
                  'yucky ogre', 'nasty troll', 'leviathan']
    weapons = ['Durandal sword', 'hammer of Kharas',
               'axe of the Dwarvish Lords']
    character = random.choice(characters)
    weapon = random.choice(weapons)
    item = 'dagger'
    intro_message(character)
    where_to_go(character, item, weapon)

if __name__ == '__main__':
    adventure_game()

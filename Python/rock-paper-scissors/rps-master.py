#!/usr/bin/env python3

import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def remember(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input('Rock, paper, scissors? > ').lower()
            if move in moves:
                return move
                break

    def remember(self, my_move, their_move):
        print(f'You Played {my_move}')
        print(f'Your Opponent played {their_move}')


class ReflectPlayer(Player):
    next_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.next_move = their_move
        return self.next_move

    def move(self):
        return self.next_move


class ExcludeMovesPlayer(Player):
    next_move = random.choice(moves)

    def learn(self, my_move, their_move):
        next_moves = ['rock', 'paper', 'scissors']
        del next_moves[next_moves.index(my_move)]
        self.next_move = random.choice(next_moves)
        return self.next_move

    def move(self):
        return self.next_move


class CyclePlayer(Player):
    next_move = moves[0]

    def learn(self, my_move, their_move):
        del moves[moves.index(my_move)]
        moves.append(my_move)
        self.next_move = moves[0]
        return self.next_move

    def move(self):
        return self.next_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p1.remember(move1, move2)
        self.p2.remember(move2, move1)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print('Player 1 wins!')
            return [1, 0]
        elif beats(move2, move1):
            print('Player 2 wins!')
            return [0, 1]
        else:
            return [0, 0]

    def number_of_rounds(self):
        print('How many rounds would you like to play? ')
        while True:
            answer = input('Please insert a number > ')
            if answer.isdigit():
                return(int(answer))
                break

    def play_game(self):
        print('Game start!')
        score1 = 0
        score2 = 0
        rounds = []
        for round in range(self.number_of_rounds()):
            print(f'Round {round+1}:')
            rounds.append(self.play_round())
            if rounds[round] == [1, 0]:
                score1 += 1
            elif rounds[round] == [0, 1]:
                score2 += 1
            else:
                print('It\'s a tie!')
            print(f'Current score:\n'
                  f'You scored {score1} points\tYour opponent scored '
                  f'{score2} points')
        print(f'\nFinal score:\nYou scored {score1} points'
              f'\tYour opponent scored {score2} points')
        if score1 > score2:
            print('Congrats, You win!')
        elif score2 > score1:
            print('You lose, game over!')
        else:
            print('Congrats, it\'s a tie!')


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice([CyclePlayer(),
                                             RandomPlayer(),
                                             ReflectPlayer(),
                                             ExcludeMovesPlayer()]))
    game.play_game()

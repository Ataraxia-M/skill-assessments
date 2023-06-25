# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 16:40:08 2023

@author: USER
"""

import os
import random
import logging

logging.basicConfig(level=logging.WARNING)

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(10)]
        self.player_symbol = ""
        self.computer_symbol = ""
        self.current_player = ""
        self.winning_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
            [1, 5, 9], [3, 5, 7]  # diagonals
        ]

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def display_board(self):
        print(" %s | %s | %s " % (self.board[1], self.board[2], self.board[3]))
        print("-----------")
        print(" %s | %s | %s " % (self.board[4], self.board[5], self.board[6]))
        print("-----------")
        print(" %s | %s | %s " % (self.board[7], self.board[8], self.board[9]))
        print()

    def choose_symbol(self):
        while True:
            symbol = input("Choose 'X' or 'O': ").upper()
            if symbol == "X" or symbol == "O":
                self.player_symbol = symbol
                self.computer_symbol = "O" if self.player_symbol == "X" else "X"
                break
            else:
                logging.warning("Invalid symbol. Please choose 'X' or 'O'.")

    def make_move(self, position, symbol):
        self.board[position] = symbol

    def get_available_moves(self):
        return [i for i in range(1, 10) if self.board[i] == " "]

    def check_winner(self, symbol):
        for combination in self.winning_combinations:
            if all(self.board[pos] == symbol for pos in combination):
                return True
        return False

    def check_draw(self):
        return " " not in self.board[1:]

    def get_player_move(self):
        while True:
            move = input("Enter your move (1-9): ")
            if move.isdigit() and 1 <= int(move) <= 9 and self.board[int(move)] == " ":
                return int(move)
            else:
                logging.warning("Invalid move. Please try again.")

    def get_computer_move(self):
        available_moves = self.get_available_moves()
        return random.choice(available_moves)

    def switch_player(self):
        self.current_player = self.computer_symbol if self.current_player == self.player_symbol else self.player_symbol

    def play_game(self):
        self.clear_screen()
        print("Welcome to Tic-Tac-Toe!")
        self.display_board()
        self.choose_symbol()
        self.current_player = "X"

        while True:
            if self.current_player == self.player_symbol:
                move = self.get_player_move()
            else:
                move = self.get_computer_move()

            self.make_move(move, self.current_player)
            self.clear_screen()
            self.display_board()

            if self.check_winner(self.current_player):
                print(f"Player {self.current_player} wins!")
                break

            if self.check_draw():
                print("It's a draw!")
                break

            self.switch_player()

        print("Game over.")

    def play_again(self):
        while True:
            choice = input("Would you like to play again? (Y/N): ").upper()
            if choice == "Y":
                self.board = [" " for _ in range(10)]
                self.current_player = ""
                self.clear_screen()
                self.play_game()
            elif choice == "N":
                print("Thank you for playing Tic-Tac-Toe!")
                break
            else:
                logging.warning("Invalid choice. Please enter 'Y' or 'N'.")

game = TicTacToe()
game.play_game()
game.play_again()

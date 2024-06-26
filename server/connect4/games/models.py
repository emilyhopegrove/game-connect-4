"""
This module defines the Game model for the Connect 4 game application.
It includes the game logic, state management, and database interactions necessary
to play and track the state of Connect 4 games.
"""

from django.db import models
from django.db.models import JSONField 
from django.core.exceptions import ValidationError
from django.db import models, transaction

def default_board():
    return [["" for _ in range(7)] for _ in range(6)]

class Game(models.Model):

    """
    Represents a single game of Connect 4, including its board state, current player,
    game status, and the winner of the game.

    Attributes:
        board (JSONField): A 6x7 grid representing the Connect 4 board.
        current_player (CharField): Indicates whose turn it is ('R' for Red, 'Y' for Yellow).
        status (CharField): The current status of the game ('ongoing' or 'finished').
        winner (CharField): The winner of the game ('R', 'Y', or 'N' for none if the game is a draw).
    """

    board = JSONField(default=default_board)  # Default 6x7 empty grid
    current_player = models.CharField(max_length=1, choices=(('R', 'Red'), ('Y', 'Yellow'))) # Track current player's turn
    status = models.CharField(max_length=10, choices=(('ongoing', 'Ongoing'), ('finished', 'Finished'))) # Track game status
    winner = models.CharField(max_length=1, choices=(('R', 'Red'), ('Y', 'Yellow'), ('N', 'None')), default='N') # Track winner of  the game

    def __str__(self):
        return f"Game {self.id} - Status: {self.status}"

    def is_board_full(self):
        """Check if the game board is full."""
        for row in self.board:
            if "" in row:
                return False
        return True

    def check_winner(self):
        """Check for a winner in the game."""
        # Check horizontal, vertical and diagonal lines for a win
        for i in range(6):  # 6 rows
            for j in range(7):  # 7 columns
                if j <= 3 and self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3] != "":
                    return self.board[i][j]
                if i <= 2 and self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j] != "":
                    return self.board[i][j]
                if i <= 2 and j <= 3 and self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3] != "":
                    return self.board[i][j]
                if i >= 3 and j <= 3 and self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2] == self.board[i-3][j+3] != "":
                    return self.board[i][j]
        return None

    def update_game_status(self):
        """Update the game status based on board state."""
        winner = self.check_winner()
        if winner:
            self.winner = winner
            self.status = 'finished'
            self.save()
        elif self.is_board_full():
            self.status = 'finished'
            self.winner = 'None'  # None for draw
            self.save()

    def validate_board(self):
        """
        Validates the structure and content of the board.

        Raises:
            ValidationError: If the board structure is not a 6x7 grid or contains invalid values.
        """
        if not isinstance(self.board, list) or len(self.board) != 6 or any(len(row) != 7 for row in self.board):
            raise ValidationError("Invalid board structure")
        for row in self.board:
            for cell in row:
                if cell not in ["", "R", "Y"]:
                    raise ValidationError("Invalid cell value in the board")

    def make_move(self, column):
        """
        Attempts to place the current player's token in the specified column.

        Args:
            co lumn (int): The column index where the current player wants to place their token.

        Raises:
            ValueError: If the column index is invalid or the column is already full.
        """
        if column < 0 or column >= 7:
            raise ValueError("Invalid column index")
        if self.board[0][column] != "":
            raise ValueError("Column is full")

        self.validate_board()  # Validate before making a move

        with transaction.atomic():  # Handle concurrent modifications
            for row in reversed(self.board):
                if row[column] == "":
                    row[column] = self.current_player
                    break
            self.save()
            self.update_game_status()


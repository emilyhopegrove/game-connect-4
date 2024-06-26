from django.test import TestCase
from .models import Game

class GameModelTest(TestCase):
    def setUp(self):
        # Set up data for the tests
        self.game = Game.objects.create()

    # def test_initial_board_setup(self):
    #     """Test that the board is initialized correctly."""
    #     expected_board = [["" for _ in range(7)] for _ in range(6)]
    #     self.assertEqual(self.game.board, expected_board)

    # def test_make_move(self):
    #     """Test making a move on the board."""
    #     self.game.make_move(0)  # Make a move in the first column
    #     self.assertEqual(self.game.board[5][0], 'R')  # Assuming 'R' starts

    # def test_game_status_after_move(self):
    #     """Test the game status after a move is made."""
    #     self.game.make_move(0)
    #     self.assertEqual(self.game.status, 'ongoing')
#works
    # def test_check_winner_no_winner(self):
    #     """Test that check_winner returns None when there is no winner."""
    #     self.assertIsNone(self.game.check_winner())

    # def test_full_board_draw(self):
    #     """Test that a full board without a winner results in a draw."""
    #     # Setup a full board with no winner
    #     self.game.board = [
    #         ['Y', 'R', 'R', 'R', 'Y', 'R', 'Y'],
    #         ['Y', 'Y', 'Y', 'R', 'R', 'R', 'Y'],
    #         ['Y', 'R', 'Y', 'Y', 'R', 'Y', 'Y'],
    #         ['R', 'Y', 'R', 'R', 'Y', 'Y', 'R'],
    #         ['Y', 'Y', 'Y', 'R', 'Y', 'R', 'Y'],
    #         ['Y', 'Y', 'Y', 'R', 'Y', 'Y', 'Y']

    #     ]
    #     self.game.update_game_status()
    #     self.assertEqual(self.game.winner, 'N', f"Expected no winner, but got {self.game.winner}")

    def validate_board_gravity(self):
        """Helper function to validate board gravity."""
        for col in range(7):  # Assuming a 7-column board
            empty_found = False
            for row in range(6):  # Check from top to bottom
                if self.game.board[row][col] == '':
                    empty_found = True
                elif empty_found and self.game.board[row][col] != '':
                    print(f"Invalid state found in column {col}, row {row}: filled cell after empty cell")
                    return False  # Immediately return False upon finding an invalid state
        return True

    def test_board_gravity_consistency(self):
        """Test that the board adheres to gravity, ensuring no filled cells are above empty cells in any column."""
        
        # Valid scenario: Should pass, there is a valid connect 4
        self.game.board = [
            ['Y', 'R', 'R', '', 'Y', 'R', 'Y'],
            ['Y', 'Y', 'Y', 'Y', 'R', 'R', 'Y'],
            ['Y', 'R', 'Y', 'Y', 'R', 'Y', 'Y'],
            ['R', 'Y', 'R', 'R', 'Y', 'Y', 'R'],
            ['Y', 'Y', 'Y', 'R', 'Y', 'R', 'Y'],
            ['Y', 'Y', 'Y', 'R', 'Y', 'Y', 'Y']
        ]
        self.assertTrue(self.validate_board_gravity(), "Connect 4!")
        # # Valid scenario: There can be an empty row so long as the columns beneath are filled and there is a valid connect 4. 
        # self.game.board = [
        #     ['', '', '', '', '', '', ''],  # Top-most row (visually at the top in the game)
        #     ['', '', '', '', '', '', ''],
        #     ['Y', 'R', 'Y', 'R', 'Y', 'R', 'Y'],
        #     ['Y', 'Y', 'Y', 'R', 'R', 'R', 'Y'],
        #     ['Y', 'R', 'Y', 'Y', 'R', 'Y', 'Y'],
        #     ['R', 'Y', 'R', 'R', 'Y', 'Y', 'Y']  # Bottom-most row (visually at the bottom in the game)
        # ]
        # self.assertTrue(self.validate_board_gravity(), "Valid scenario. There can be an empty row so long as the columns beneath are filled and there is a valid connect 4. ")
        
        # # Valid scenario: Diagonal connect 4 
        # self.game.board = [
        #     ['Y', 'Y', '', 'R', 'R', 'Y', 'R'],
        #     ['Y', 'Y', '', 'R', 'R', 'R', 'Y'],
        #     ['R', 'R', 'Y', 'Y', 'R', 'Y', 'Y'],
        #     ['Y', 'Y', 'R', 'Y', 'Y', 'Y', 'R'],
        #     ['Y', 'Y', 'Y', 'R', 'Y', 'R', 'Y'],
        #     ['Y', 'Y', 'R', 'R', 'Y', 'Y', 'Y']
        # ]
        # self.assertTrue(self.validate_board_gravity(), "Valid scenario. Diagonal connect 4 is valid.")
        
        #  # Valid scenario: Backwards diagonal connect 4
        # self.game.board = [
        #     ['', '', '', '', '', '', ''],
        #     ['Y', 'Y', '', 'R', 'R', 'R', 'Y'],
        #     ['Y', 'R', '', 'Y', 'R', 'Y', 'Y'],
        #     ['Y', 'Y', '', 'R', 'Y', 'Y', 'R'],
        #     ['Y', 'Y', 'R', 'R', 'Y', 'R', 'Y'],
        #     ['Y', 'Y', 'Y', 'R', 'Y', 'Y', 'Y']
        # ]
        # self.assertTrue(self.validate_board_gravity(), "Valid scenario. There can be an empty row so long as the columns beneath are filled and there is a valid connect 4. ")
        
        # # Invalid scenario: Floating 'R' should fail
        # self.game.board = [
        #     ['', '', '', '', '', '', ''],
        #     ['', '', '', '', '', '', ''],
        #     ['', '', '', '', '', '', ''],
        #     ['', '', 'R', '', '', '', ''],
        #     ['', '', '', '', '', '', ''],
        #     ['', '', '', '', '', '', '']
        # ]
        # self.assertFalse(self.validate_board_gravity(), "Floating full cell scenario should fail.")

        # # Scenario 2: Should fail when an empty cell has a filled cell above it
        # self.game.board = [
        #     ['Y', 'R', 'R', 'R', 'Y', 'R', 'Y'],
        #     ['Y', 'Y', 'Y', 'R', 'R', 'R', 'Y'],
        #     ['Y', 'R', 'Y', 'Y', 'R', 'Y', 'Y'],
        #     ['R', 'Y', 'R', 'R', 'Y', 'Y', 'R'],
        #     ['Y', 'Y', 'Y', 'R', 'Y', 'R', 'Y'],
        #     ['Y', 'Y', 'Y', 'R', 'Y', 'Y', '']
        # ]
        # self.assertFalse(self.validate_board_gravity(), "There cannot be an empty cell with a filled cell above it.")

        # # Scenario 3: Should pass, space above a filled cell can exist in real life 
        # self.game.board = [
        #     ['Y', '', 'R', 'R', 'Y', 'R', 'Y'],
        #     ['Y', 'R', 'Y', 'R', 'R', 'R', 'Y'],
        #     ['Y', 'R', 'Y', 'Y', 'R', 'Y', 'Y'],
        #     ['R', 'Y', 'R', 'R', 'Y', 'Y', 'R'],
        #     ['Y', 'Y', 'Y', 'R', 'Y', 'R', 'Y'],
        #     ['Y', 'Y', 'Y', 'R', 'Y', 'Y', 'Y']
        # ]
        # self.assertTrue(self.validate_board_gravity(), "There can be an empty cell with a column of filled cells below it.")

    # # Add more tests as needed for other methods and edge cases



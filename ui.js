// ui.js

// This file handles the user interface for the Connect 4 game.
// It displays the game board, player information, and interactions.

// Import necessary components
const board = require('./board');
const game = require('./game');
const player = require('./player');

// Initialize the game board
const boardComponent = new board.Board();

// Initialize players
const player1 = new player.Player('Player 1', 'X');
const player2 = new player.Player('Player 2', 'O');

// Set up the game
const gameInstance = new game.Game(boardComponent, player1, player2);

// Render the initial game board
boardComponent.render();

// Handle player interactions
document.addEventListener('click', (event) => {
  // Get the column index from the clicked element
  const columnIndex = event.target.dataset.column;

  // Make the move
  gameInstance.makeMove(columnIndex);
});

// Update the game board and player information after each move
gameInstance.onMoveMade(() => {
  boardComponent.render();
  // Update player information (e.g., current turn, score)
});

// Handle game over
gameInstance.onGameOver((winner) => {
  // Display the winner or tie message
  console.log(`Game Over: ${winner ? winner.name : 'It\'s a tie!'}`);
  // Reset the game if desired
});


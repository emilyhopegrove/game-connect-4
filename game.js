// game.js

// Initialize the game board
const board = new Board();

// Initialize players
const player1 = new Player('Player 1', 'X');
const player2 = new Player('Player 2', 'O');

// Set the current player
let currentPlayer = player1;

// Game loop
while (true) {
  // Render the board
  board.render();

  // Get the player's move
  const column = currentPlayer.getMove();

  // Drop the piece into the column
  board.dropPiece(column, currentPlayer.piece);

  // Check for a win
  if (board.checkWin()) {
    console.log(`Player ${currentPlayer.name} wins!`);
    break;
  }

  // Check for a tie
  if (board.isFull()) {
    console.log('It\'s a tie!');
    break;
  }

  // Switch players
  currentPlayer = currentPlayer === player1 ? player2 : player1;
}


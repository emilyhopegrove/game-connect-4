// board.js

// This file manages the game board, rendering the grid, and updating it based on player moves.

// Initialize the game board as a 6x7 grid
let board = [];
for (let i = 0; i < 6; i++) {
  board.push([]);
  for (let j = 0; j < 7; j++) {
    board[i].push(null);
  }
}

// Function to render the game board
function renderBoard() {
  // Clear the board container
  const boardContainer = document.getElementById('board-container');
  boardContainer.innerHTML = '';

  // Create table rows and cells
  for (let i = 0; i < 6; i++) {
    const row = document.createElement('div');
    row.className = 'row';
    for (let j = 0; j < 7; j++) {
      const cell = document.createElement('div');
      cell.className = 'cell';
      if (board[i][j] === null) {
        cell.textContent = '';
      } else if (board[i][j] === 'X') {
        cell.textContent = 'X';
      } else if (board[i][j] === 'O') {
        cell.textContent = 'O';
      }
      row.appendChild(cell);
    }
    boardContainer.appendChild(row);
  }
}

// Function to update the board based on player moves
function updateBoard(column, player) {
  // Find the first available row in the selected column
  for (let i = 5; i >= 0; i--) {
    if (board[i][column] === null) {
      board[i][column] = player;
      break;
    }
  }
  renderBoard();
}

// Render the initial board
renderBoard();


// utils.js

// Utility functions for the Connect 4 game

// Function to create a 2D array (grid) with specified dimensions
function createGrid(rows, cols) {
  const grid = [];
  for (let i = 0; i < rows; i++) {
    grid[i] = [];
    for (let j = 0; j < cols; j++) {
      grid[i][j] = null; // Initialize all cells as null
    }
  }
  return grid;
}

// Function to print the grid to the console
function printGrid(grid) {
  for (let i = 0; i < grid.length; i++) {
    console.log(grid[i].join(' | '));
  }
}

// Function to check if a cell is empty
function isEmptyCell(grid, row, col) {
  return grid[row][col] === null;
}

// Function to get the next available row in a column
function getNextAvailableRow(grid, col) {
  for (let i = grid.length - 1; i >= 0; i--) {
    if (isEmptyCell(grid, i, col)) {
      return i;
    }
  }
  return -1; // Column is full
}

// Function to drop a piece into a column
function dropPiece(grid, col, piece) {
  const row = getNextAvailableRow(grid, col);
  if (row !== -1) {
    grid[row][col] = piece;
    return true;
  }
  return false; // Column is full
}

// Function to check for a win
function checkWin(grid, piece) {
  // Implement the logic to check for a win here
  // ...
  return false; // No win
}

// Function to check for a tie
function checkTie(grid) {
  // Implement the logic to check for a tie here
  // ...
  return false; // Not a tie
}

export { createGrid, printGrid, isEmptyCell, getNextAvailableRow, dropPiece, checkWin, checkTie };


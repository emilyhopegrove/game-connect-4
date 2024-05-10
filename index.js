// index.js
// Entry point of the game where you initialize the game and start the application.

// Import necessary components
const Game = require('./game');
const Board = require('./board');
const Player = require('./player');
const UI = require('./ui');

// Initialize the game
const game = new Game();
const board = new Board();
const player1 = new Player('Player 1', 'X');
const player2 = new Player('Player 2', 'O');
const ui = new UI(board, player1, player2);

// Start the game
game.start(board, player1, player2, ui);


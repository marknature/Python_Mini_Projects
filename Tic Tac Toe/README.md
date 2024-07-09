# Tic Tac Toe Game with GUI using Tkinter

## Description

This project implements a classic Tic Tac Toe game (also known as Noughts and Crosses) using Python's Tkinter library to create a graphical user interface (GUI). The game can be played either against another player or against the computer.

## Features

- **Two Game Modes:** 
  - Single-player mode against the computer.
  - Two-player mode.
- **Intelligent Computer Opponent:** The system uses a basic strategy to either win or prevent the player from winning.
- **Graphical User Interface:** Built using Tkinter, the game has an interactive and easy-to-use GUI.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter library (usually included with Python)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/tic-tac-toe.git
    ```
2. Navigate to the project directory:
    ```sh
    cd tic-tac-toe
    ```
3. Run the game:
    ```sh
    python tic_tac_toe.py
    ```

## Usage

1. When you start the game, you will be presented with a landing page where you can choose between single-player and multiplayer modes.
2. The game board is a 3x3 grid where players take turns clicking on tiles to place their marks (X or O).
3. The game will automatically check for a win, loss, or tie and display an appropriate message.

## Code Overview

- **Main Functions:**
  - `gameboard_pc()`: Sets up the game board for playing against the computer.
  - `gameboard_pl()`: Sets up the game board for playing against another player.
  - `get_text_pc()`, `get_text()`: Handle text placement on the game board buttons when clicked.
  - `pc()`: Determines the computer's next move.
  - `winner()`: Checks if a player has won the game.
  - `isfree()`: Checks if a tile is free to place a mark.
  - `isfull()`: Checks if the board is full, indicating a tie.

## Example GUI

### Single-Player Mode

![GUI 1](https://github.com/marknature/Python_Mini_Projects/blob/main/Tic%20Tac%20Toe/img/Screenshot2.png)

### Two-Player Mode

![GUI 2](https://github.com/marknature/Python_Mini_Projects/blob/main/Tic%20Tac%20Toe/img/Screenshot1.png)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- This project uses the Tkinter library for GUI components.

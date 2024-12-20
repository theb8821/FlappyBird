
# Flappy Bird - Python Game

Flappy Bird is a classic arcade-style game developed using Python and Pygame. The goal of the game is to keep the bird in the air by pressing the spacebar to flap its wings and avoid obstacles (pipes) while trying to achieve the highest possible score.

## Project Structure

This project is organized into several files for clarity and ease of maintenance:

```
FlappyBird/
│
├── main.py              # Entry point; the main game loop
├── bird.py              # Class for the bird
├── pipe.py              # Class for pipes
├── game.py              # Handles game logic and state
├── assets/              # Folder to store images, sounds, etc.
│   ├── background.png
│   ├── bird.png
│   ├── pipe.png
│   └── ...
└── README.md            # Project description, setup instructions
```

### Game Components:
1. **Bird**: The player controls the bird, which can move up by flapping its wings. The bird is affected by gravity, and the objective is to avoid hitting the pipes.
2. **Pipes**: Pipes move from right to left, and the player must navigate the bird through gaps between the pipes.
3. **Game**: The game logic handles the bird's movement, pipe generation, collision detection, and score tracking.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/theb8821/FlappyBird.git
   ```

2. **Navigate to the project folder**:
   ```bash
   cd FlappyBird
   ```

3. **Install Pygame** (make sure Python is installed):
   ```bash
   pip install pygame
   ```

4. **Add Assets**: Make sure you have the game assets (images like `bird.png`, `background.png`, and `pipe.png`) placed in the `assets/` folder. You can use any Flappy Bird-themed images you find or create your own.

## Running the Game

To play the game, simply run the `main.py` file:

```bash
python main.py
```

Use the **spacebar** to make the bird flap and navigate through the pipes. The game will continue until the bird hits a pipe or the ground.

## Controls

- **Spacebar**: Flap the bird upwards to avoid obstacles.

## Features

- **Dynamic pipe generation**: Pipes are generated with random heights and move from right to left.
- **Collision detection**: The game ends if the bird collides with a pipe or hits the ground.
- **Score tracking**: The score increases each time the bird successfully passes through a gap between pipes.
- **Game over screen**: When the game ends, the score is displayed.

## Customizing the Game

You can easily customize the game by modifying the following:
- **Pipe speed**: Change the speed of pipe movement in `pipe.py`.
- **Gravity and lift**: Adjust the bird's gravity and flap strength in `bird.py`.
- **Background and assets**: Replace the default assets in the `assets/` folder with your own images.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The original Flappy Bird game by Dong Nguyen.
- Pygame library for providing the tools to create this game in Python.

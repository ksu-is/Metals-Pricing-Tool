# Chicken Crossing Chaos

## Introduction
Welcome to **Chicken Crossing Chaos**, a hilariously chaotic 2D arcade game developed by **ChillHack Jake**, a passionate web developer from Hong Kong. In this game, you take control of a quirky chicken trying to cross a bustling highway filled with speeding cars while collecting tasty corn for points. With its simple yet addictive gameplay, funny sound effects (logged as text), and wacky events like random pigeons stealing corn, this game is designed to keep you entertained for hours!

### Game Features
- **Dynamic Gameplay**: Dodge cars, collect corn, and survive as long as you can to rack up a high score.
- **Difficulty Settings**: Choose from Easy, Medium, or Hard modes to adjust car speed and count.
- **Color Schemes**: Customize the game with Classic, Night, or Sunset themes for different visual vibes.
- **Pause Menu**: Pause the game at any time to continue or return to the main menu.
- **Game Over Screen**: View your final score and choose to restart or return to the menu.
- **Humorous Events**: Enjoy random events like pigeons stealing corn and funny messages to keep you chuckling.
- **Robust Error Handling**: Built with logging to ensure smooth gameplay and easy debugging.

## Installation Tutorial
Follow these steps to set up and run **Chicken Crossing Chaos** on your computer.

### Prerequisites
- **Python 3.12.10**: The game is built and tested with Python 3.12.10.
- **Pygame 2.6.1**: The game uses Pygame for graphics and input handling.
- A compatible operating system (Windows, macOS, or Linux).

### Step-by-Step Installation
1. **Install Python**:
   - Download Python 3.12.10 from the [official Python website](https://www.python.org/downloads/release/python-31210/).
   - Follow the installation instructions for your operating system.
   - Ensure you check the option to add Python to your system PATH during installation.
   - Verify the installation by opening a terminal/command prompt and running:
     ```
     python --version
     ```
     You should see `Python 3.12.10`.

2. **Install Pygame**:
   - Open a terminal/command prompt and install Pygame 2.6.1 using pip:
     ```
     pip install pygame==2.6.1
     ```
   - Verify the installation by running:
     ```
     python -c "import pygame; print(pygame.__version__)"
     ```
     You should see `2.6.1`.

3. **Download the Game**:
   - Clone or download the game repository from its source (e.g., GitHub).
   - Alternatively, save the game code as `chicken_crossing.py` in a directory of your choice.
   - Ensure the game file is in a directory where you have write permissions (e.g., your home directory).

4. **Run the Game**:
   - Navigate to the directory containing `chicken_crossing.py` in your terminal/command prompt:
     ```
     cd path/to/game/directory
     ```
   - Run the game using Python:
     ```
     python chicken_crossing.py
     ```
   - The game window should open, displaying the main menu.

### Troubleshooting Installation
- **Python not found**: Ensure Python is added to your PATH. Reinstall Python and check the PATH option.
- **Pygame not found**: Verify Pygame installation with `pip show pygame`. Reinstall if necessary.
- **Game crashes**: Check the console for error messages or logs (saved in the terminal or a log file). Common issues include missing dependencies or incorrect Python/Pygame versions.
- **Permission issues**: Ensure you have write permissions in the game directory, or run the terminal as an administrator.

## Game Tutorial
This tutorial will guide you through the gameplay mechanics, controls, and features of **Chicken Crossing Chaos**.

### Main Menu
When you start the game, you'll see the main menu with the following options:
- **Start Game**: Press `S` to begin playing with the selected settings.
- **Difficulty**: Press `D` to cycle through difficulty settings:
  - **Easy**: 3 cars, slower speed (3 pixels/frame).
  - **Medium**: 4 cars, moderate speed (5 pixels/frame).
  - **Hard**: 6 cars, faster speed (7 pixels/frame).
- **Color Scheme**: Press `C` to cycle through visual themes:
  - **Classic**: Black background, white chicken.
  - **Night**: Dark blue background, light blue chicken.
  - **Sunset**: Reddish background, pale yellow chicken.

### Gameplay
Your goal is to guide the chicken across a busy highway, avoiding cars and collecting corn to earn points.

#### Controls
- **Arrow Keys**:
  - **Left/Right**: Move the chicken horizontally.
  - **Up/Down**: Move the chicken vertically.
- **P**: Pause the game to access the pause menu.
- **R** (Game Over only): Restart the game with the same settings.
- **M** (Pause or Game Over): Return to the main menu.

#### Objectives
- **Avoid Cars**: Cars move horizontally across the screen. Colliding with a car reduces your lives by 1. You start with 3 lives.
- **Collect Corn**: Yellow corn pieces appear randomly. Collecting corn adds 10 points to your score.
- **Survive**: Keep the chicken alive as long as possible to achieve a high score.

#### Pause Menu
- Press `P` during gameplay to pause.
- The pause menu displays:
  - **Continue**: Press `C` to resume the game.
  - **Return to Menu**: Press `M` to go back to the main menu.

#### Game Over
- When you lose all 3 lives, the game ends, and the Game Over screen appears, showing your final score.
- Options:
  - **Restart**: Press `R` to start a new game with the same difficulty and color scheme.
  - **Return to Menu**: Press `M` to go back to the main menu.

#### Funny Events
- **Random Pigeon**: Occasionally, a pigeon steals a corn piece, adding a new one elsewhere (1% chance per frame).
- **Humorous Messages**: Collecting corn or other events triggers funny messages like "Why did the chicken join a band? It had the drumsticks!" (displayed in the console/log).

### Tips for Success
- **Time Your Moves**: Watch the cars' patterns to find safe gaps for crossing.
- **Prioritize Corn**: Collecting corn boosts your score, but don’t risk a collision.
- **Use Pause Strategically**: Pause the game (`P`) to plan your next move if things get hectic.
- **Start with Easy**: If you’re new, try the Easy difficulty to get a feel for the game.

## Developer Information
**Chicken Crossing Chaos** was created by **ChillHack Jake**, a web developer based in Hong Kong. With a passion for creating fun and engaging games, Jake combined his programming skills and love for humor to craft this chaotic chicken adventure.

- **Contact**: Reach out via [GitHub](https://github.com/ChillHackLab) or email (info@chillhack.net) for feedback or inquiries.
- **Contributions**: Want to contribute? Check the repository for issues or submit pull requests with improvements or bug fixes.

## Support the Developer
If you like this game, please buy me a coffee!

**BTC**: 3MNNntE4NtKiiwWEutXSPitVhubfuBeLLr

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- **Pygame Community**: Thanks for providing an awesome library for game development.
- **Inspiration**: Classic arcade games like Frogger and the timeless "Why did the chicken cross the road?" joke.

---

Happy clucking, and enjoy the chaos!

# tetris-autoplayer
🎮 Overview: This repository contains an AI-powered autoplayer for a Tetris-like game. The AI strategically selects moves to optimize gameplay by analyzing the board state and making real-time decisions to achieve the highest possible score.

The core of the AI revolves around evaluating board configurations after simulated moves and selecting the best sequence of actions based on a calculated score. This score takes into account various factors such as height, cleared lines, holes, and bumpiness.

🧠 Features: Advanced Move Selection - The AI uses a scoring system that evaluates potential moves based on factors like board height, line clears, and holes. Adaptive Strategy - Depending on the current game state, the AI adapts its strategy, including the ability to use special actions like bombing when necessary. Board Simulation - The AI simulates potential board states after different sequences of moves and rotations to select the optimal strategy.

🚀 Getting Started - Prerequisites: Ensure you have Python installed on your machine. This project is compatible with any recent version of Python3.

Copy code Once you are in the code directory, you should be able to start the interface by running: python visual.py To get a feeling for the game, you can also run any of the interfaces in manual mode by adding the flag -m: python visual.py -m This will start the server and the AI will begin to make automated decisions based on the game board state. You can also use a Pygame-based interface; run python visual-pygame.py to use it. For this, you need to have a working copy of Pygame; run: pip --user install pygame to install it.

🛠️ Customization: You can adjust the AI's behavior by modifying the weights used in the calculate_score function within player.py. These weights influence how the AI prioritizes different aspects of the board, such as height, cleared lines, holes, and bumpiness.

Files Overview: player.py: Contains the AI logic, including decision-making and scoring functions. adversary.py: Handles adversary simulation if applicable. server.py: Manages the game loop and interactions between the AI and the game. constants.py: Defines constants such as game parameters and scoring weights.

🤝 Contributing: Contributions are welcome! Feel free to fork this repository and submit a pull request with your improvements or new features.

📄 License: This project is licensed under the MIT License - see the LICENSE file for details.

📧 Contact: For any inquiries or feedback, reach out to me via LinkedIn.

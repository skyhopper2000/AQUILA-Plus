# Aquila Plus

### Artificial
### Quizmaster
### User
### Interface
### Learning
### Assistant

Aquila Plus is a Python-based application designed for managing and practicing gameshow style questions. This iteration is specifically designed for AMEC bible quizzing. The project features modular code for handling graphics, utilities, sound (buzzer), and question data, with a focus on extensibility and ease of use.

## Features
- **Question Management:** Organized question data by season and week for easy access and updates.
- **Graphics Module:** Handles visual presentation, likely for displaying questions and scores.
- **Buzzer Support:** Integrates sound effects for game show-style interactions.
- **Utilities:** Common helper functions to streamline code and avoid repetition.
- **Extensible Data Structure:** Easily add new seasons, weeks, or question sets.

## Project Structure
```
aquila_graphics.py        # Graphics and display logic
aquila_utils.py           # Utility functions
buzzer.py                 # Buzzer/sound effect logic
fromPyCompiler.py         # (Purpose unclear, possibly for compiling or parsing)
globals.py                # Global variables and constants
main.py                   # Entry point for the application
model.py                  # Data models and structures
assets/images/            # Image assets for the application
question_data/season_26/  # Organized question sets by week
```

## Getting Started
1. **Requirements:**
   - Python 3.10 or higher
   - pygame
   - pyttsx3
   - importlib.util

2. **Running the Application:**
   ```bash
   python main.py
   ```

3. **Adding Questions:**
   - Place new question files in the appropriate `question_data/season_xx/weekN.py` directory.
   - Follow the format used in existing week files.

## Contributing
Contributions are welcome! Please follow standard Python best practices and keep code modular.

## License
Specify your license here (e.g., MIT, GPL, etc.).

## Author
Quentin Frank
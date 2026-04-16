# Tkinter Microwave

An educational Python interface meant to mimic a real microwave. Demonstrates basic Python knowledge by:

- **Tkinter** — Creating and displaying a Tkinter interface with interactable buttons.
- **UI/UX** — Thoughtfully positioning elements on the application into a user friendly grid.
- **Conditionals** — Displaying an image and changing it based on conditionals.
- **Scheduling** — Using event loop scheduling functions to create a functioning timer.
- **String manipulation** — String manipulation and casting to keep track of minutes and seconds.
- **Sound generation** — Using winsound to play tones at specific frequencies for a set duration.

# Features
- **Start / Stop Controls** — Start a countdown timer and cancel it mid-cycle at any time.
- **Live Countdown Display** — The timer updates in real time, showing remaining minutes and seconds in `MM:SS` format.
- **Interaction Beep** — Plays an audible tone via `winsound` when a button is pressed.
 
## Requirements

**Python 3**

> This project uses `winsound`, which is only available on **Windows**. The beep functionality will not work on macOS or Linux.

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/alex-jns/tkinter-microwave.git
   cd tkinter-microwave
   ```

2. **Confirm Python is installed**
   ```bash
   python --version
   ```
   Python 3.x is required. No third-party packages need to be installed.

3. **Run the application**
   ```bash
   python main.py
   ```

## Usage

1. **Enter a time** using the number buttons on the keypad (e.g. press `1`, `3`, `0` for 1 minute and 30 seconds).
2. **Open the door** using the buttons on the right side, and optionally add food.
3. **Press Start** to begin the countdown.
4. **Watch the timer** count down in real time on the display.
5. Press **Stop/Cancel** at any time to halt the timer and reset the display.
6. Once the timer is **finished** you may open the door and remove the food.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

````markdown
# Mouse Mover

A lightweight Python script that periodically moves your mouse to simulate activity.  
This helps prevent your computer from going idle, locking, or entering sleep mode due to inactivity.

## Features
- ⏱️ Move the mouse every **X minutes** (customisable).
- 🎲 Adds small random offsets to make movement appear natural.
- 🖥️ Works on **Windows, macOS, and Linux**.
- 🛑 Stop anytime with **Ctrl+C**.

## Requirements
- Python 3.7+
- [pyautogui](https://pyautogui.readthedocs.io/)

Install with:
```bash
pip install pyautogui
````

## Usage

### Run the script

```bash
python mouse_mover.py
```

### Change interval

By default, the mouse moves every **5 minutes**.
To change this, edit the following line in `mouse_mover.py`:

```python
move_mouse_every_x_minutes(5)
```

Example:

```python
move_mouse_every_x_minutes(2)  # every 2 minutes
```

### Example output

```
Mouse mover started. Moving every 5 minutes. Press Ctrl+C to stop.
Mouse moved to: (1024, 580)
Mouse moved to: (1132, 612)
...
```

## Notes

* On macOS, you may need to grant accessibility permissions:
  `System Preferences → Security & Privacy → Accessibility`.
* For background/automatic runs, consider using **Task Scheduler** (Windows) or **cron jobs** (macOS/Linux).

## Project Structure

```
mouse-mover-python/
│── mouse_mover.py      # Main script
│── requirements.txt    # Dependencies
│── README.md           # Documentation
└── .gitignore          # Git ignore file
```

## License

This project is licensed under the **MIT License** – free to use and modify.

```


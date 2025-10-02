import pyautogui
import time
import random

def move_mouse_every_x_minutes(x_minutes=5):
    print(f"Mouse mover started. Moving every {x_minutes} minutes. Press Ctrl+C to stop.")
    try:
        while True:
            # Get current mouse position
            x, y = pyautogui.position()

            # Move mouse a small random offset (so it looks natural)
            dx = random.randint(-100, 100)
            dy = random.randint(-100, 100)

            pyautogui.moveTo(x + dx, y + dy, duration=0.5)
            print(f"Mouse moved to: ({x + dx}, {y + dy})")

            # Wait for X minutes before moving again
            time.sleep(x_minutes * 60)
    except KeyboardInterrupt:
        print("\nMouse mover stopped.")

if __name__ == "__main__":
    # Change the number to how many minutes you want
    move_mouse_every_x_minutes(5)

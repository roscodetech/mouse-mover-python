import pyautogui, time, random, platform, subprocess, ctypes

pyautogui.FAILSAFE = True  # move to top-left to abort
WIGGLE_SECONDS = 30        # every 30 s is safer than 5 min

def nudge_mouse():
    x, y = pyautogui.position()
    dx = random.randint(-20, 20)
    dy = random.randint(-20, 20)
    # keep within bounds
    sx, sy = pyautogui.size()
    nx = max(1, min(sx - 2, x + dx))
    ny = max(1, min(sy - 2, y + dy))
    pyautogui.moveTo(nx, ny, duration=0.25)

def light_key():
    # shift is usually harmless
    pyautogui.press('shift')

def prevent_sleep_platform():
    osname = platform.system()
    if osname == "Windows":
        ES_CONTINUOUS = 0x80000000
        ES_SYSTEM_REQUIRED = 0x00000001
        ES_DISPLAY_REQUIRED = 0x00000002
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)
    elif osname == "Darwin":
        return subprocess.Popen(["caffeinate", "-dimsu"])
    return None  # Linux users can run systemd-inhibit around the script

def main():
    print("Awake helper started. Ctrl+C to stop.")
    caffeinate_proc = prevent_sleep_platform()
    try:
        while True:
            nudge_mouse()
            light_key()
            time.sleep(WIGGLE_SECONDS)
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        if caffeinate_proc:
            caffeinate_proc.terminate()
        if platform.system() == "Windows":
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)  # ES_CONTINUOUS only, restore

if __name__ == "__main__":
    main()

import pyray as rl
import os
import subprocess
import sys
import json
from tkinter import Tk, filedialog

def select_project():
    root = Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title="Select Project Folder")
    root.destroy()
    return folder

def setup_project(path):
    # Split into folders and files
    folders = ["assets", "scripts", "sfx", "data", "json", "data/dialogue"]
    files = ["game.json", "runtime.py", "json/player.json", "data/dialogue/test_dialogue.json"]

    # Create the directories
    for folder in folders:
        os.makedirs(os.path.join(path, folder), exist_ok=True)

    # Create the actual files
    for filename in files:
        file_path = os.path.join(path, filename)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                if filename == "game.json":
                    f.write('{\n    "title": "New Game",\n    "version": "1.0.0",\n    "target platforms": ""\n}')
                elif filename == "runtime.py":
                    f.write('import pyray as rl\n\n# Your game logic goes here')

                elif filename == "json/player.json":
                    f.write('{\n    "tile_name": "player",\n    "spritesheetpath": "TheEngineWillSplitFrames",\n    "moveset": "D = RIGHT, A = LEFT, SPACE = JUMP,"}')

                elif filename == "data/dialogue/test_dialogue.json":
                    f.write('{\n    "Player.Dial1": Hi! The creator of this is Propro9!,\n    "ThisisHowItsMade": Hi again :],\n}')

# select project
project = select_project()

if project:
    setup_project(project)

    # run engine.py in the SAME directory as main.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    engine_path = os.path.join(base_dir, "engine.py")

    # Check if engine.py exists before running to avoid errors
    if os.path.exists(engine_path):
        subprocess.run([sys.executable, engine_path, project])
        sys.exit()
    else:
        print(f"Error: Could not find {engine_path}")

# fallback window if user cancels
rl.init_window(400, 300, "Game Launcher") # Slightly wider for better text fit
rl.set_target_fps(60)

while not rl.window_should_close():
    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)

    rl.draw_text("No project selected", 100, 140, 20, rl.GRAY)
    rl.draw_text("Close this window to exit", 105, 170, 10, rl.LIGHTGRAY)

    rl.end_drawing()

rl.close_window()
